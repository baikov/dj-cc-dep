from django.urls import path
from .views import (CountryListView, CountryDetailView, FlagDetailView,
                    FlagListView, index, ColorsListView,
                    colors_group, colors_count)

app_name = "countries"
urlpatterns = [
    path("", index, name="index"),
    path('countries/', CountryListView.as_view(), name='countries-list'),
    path('flags/', FlagListView.as_view(), name='flags-list'),
    path('colors/', ColorsListView.as_view(), name='colors-list'),
    # path('colors/<str:color_group>/', ColorGroupListView.as_view(), name='color-detail'),
    path('colors/<str:color_group>/', colors_group, name='colors-group'),
    path('colors/count/<int:color_count>/', colors_count, name='colors-count'),
    path('country/<slug:slug>/', CountryDetailView.as_view(), name='country-detail'),
    path('flag/<slug:slug>/', FlagDetailView.as_view(), name='flag-detail'),
]
