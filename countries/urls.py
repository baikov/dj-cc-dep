from django.urls import path
from .views import CountryListView, CountryDetailView

app_name = "countries"
urlpatterns = [
    # path("", index, name="index"),
    path('', CountryListView.as_view(), name='countries-list'),
    path('<slug:slug>/', CountryDetailView.as_view(), name='country-detail'),
]
