from django.urls import path
from .views import CountryListView, CountryDetailView, FlagDetailView, FlagListView, index

app_name = "countries"
urlpatterns = [
    path("", index, name="index"),
    path('countries/', CountryListView.as_view(), name='countries-list'),
    path('flags/', FlagListView.as_view(), name='flags-list'),
    path('country/<slug:slug>/', CountryDetailView.as_view(), name='country-detail'),
    path('flag/<slug:slug>/', FlagDetailView.as_view(), name='flag-detail'),
]
