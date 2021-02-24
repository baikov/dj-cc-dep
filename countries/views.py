# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import Http404
# from django.urls import reverse
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import UpdateView

from .models import Country, Flag


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
        return flags.order_by('-country')


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
        # context['country'] = self.object.country_set.all()
        return context
