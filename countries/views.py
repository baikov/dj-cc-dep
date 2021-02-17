# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
from django.shortcuts import render
# from django.urls import reverse
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import UpdateView

from .models import Country


def index(request):
    homepage_post_list = []
    context = {'countries': homepage_post_list}
    return render(request, 'countries/index.html', context)

class CountryListView(ListView):
    template_name = 'countries/countries-list.html'
    context_object_name = 'countries'
    paginate_by = 20


class CountryDetailView(DetailView):
    model = Country
    template_name = 'countries/country-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = 'Sart'
        return context
