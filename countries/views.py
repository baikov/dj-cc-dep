# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
# from django.urls import reverse
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import UpdateView
from django.db.models import Count

from .models import Color, Country, Flag, HistoricalFlag, BorderCountry


def index(request):
    homepage_countries = Country.objects.order_by('-name')[:5]
    homepage_flags = Flag.objects.order_by('-title')[:5]

    context = {'countries': homepage_countries, 'flags': homepage_flags}
    return render(request, 'countries/index.html', context)


class CountryListView(ListView):
    model = Country
    template_name = 'countries/countries-list.html'
    context_object_name = 'countries'
    paginate_by = 20

    def get_queryset(self):
        countries = Country.objects.all()
        # limit = 40
        if not self.request.user.is_superuser:
            countries = countries.published()
        return countries.order_by('-name')  # [:limit]


class FlagListView(ListView):
    model = Flag
    template_name = 'countries/flags-list.html'
    context_object_name = 'flags'
    paginate_by = 20

    def get_queryset(self):
        flags = Flag.objects.all()
        if not self.request.user.is_superuser:
            flags = flags.published()
        return flags.order_by('country__name')


class CountryDetailView(DetailView):
    model = Country
    template_name = 'countries/country-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = 'Sart'
        context['flags'] = self.object.flags.all()
        if not self.request.user.is_superuser and not self.object.is_published:
            raise Http404
        return context


class FlagDetailView(DetailView):
    model = Flag
    template_name = 'countries/flag-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        border_countries = []
        context['historical'] = HistoricalFlag.objects.filter(
            country__iso_code_a2=self.object.country.iso_code_a2).order_by('from_year')

        neighbours = BorderCountry.objects.filter(country=self.object.country)
        for row in neighbours:
            border_countries.append(row.border_country)

        context['neighbours'] = neighbours
        border_flags = Flag.objects.filter(country__in=border_countries)
        context['border_flags'] = border_flags
        context['widths'] = ['w20', 'w40', 'w80', 'w160', 'w320', 'w640', 'w1280', 'w2560']
        context['heights'] = ['h20', 'h24', 'h40', 'h60', 'h80', 'h120', 'h240']

        return context


class ColorsListView(ListView):
    model = Color
    template_name = 'countries/colors-list.html'
    context_object_name = 'colors'

    def get_queryset(self):
        colors = Color.objects.all().order_by('color_group')
        return colors


def colors_group(request, color_group):
    template_name = 'countries/colors-group.html'
    # flags = Flag.objects.filter(colors__color_group=color_group)
    url_color = color_group.split('-')
    # flags = Flag.objects.filter(colors__color_group__in=url_color).distinct()

    flags = Flag.objects.all()
    for color in url_color:
        flags = flags.filter(colors__color_group=color)
    colors = Color.objects.filter(color_group__in=url_color).distinct('color_group')

    context = {'flags': flags, 'colors': colors}
    if flags:
        return render(request, template_name, context)
    else:
        raise Http404


def colors_count(request, color_count):
    template_name = 'countries/colors-count.html'
    flags = Flag.objects.annotate(num_colors=Count('colors')).filter(num_colors=color_count)
    context = {'flags': flags, 'color_count': color_count}
    if flags:
        return render(request, template_name, context)
    else:
        raise Http404
