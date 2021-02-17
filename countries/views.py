from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

# from .models import Part


# Create your views here.
# def index(request):
#     template = 'countries/index.html'
#     parts_import_list = [1,2,3]
#     context = parts_import_list
#     return render(request, template, context)

def index(request):
    homepage_post_list = ['Spain','France','Russia']
    context = {'countries': homepage_post_list}
    return render(request, 'countries/index.html', context)