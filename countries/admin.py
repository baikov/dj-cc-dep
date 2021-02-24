from django.contrib import admin
from .models import Country, Flag, Color
from django.forms import TextInput
from django.db import models


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'is_published')
    list_filter = ['name']
    search_fields = ['name']
    readonly_fields = ['updated_date', 'created_date']
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'conventional_long_name', 'local_long_name', 'local_short_name',
                           'capital_name', 'continent', 'anthem', 'motto', 'official_language', 'national_language',
                           'internet_tld', 'currency_name', 'currency_code', 'currency_simbol', 'iso_code_a2',
                           'iso_code_a3', 'iso_code_num',
                           ]
                }),
        ('SEO', {'fields': ['meta_title', 'meta_description', 'meta_keywords', 'meta_h1', 'is_published', 'is_index',
                            'is_follow', 'created_date', 'updated_date',
                            ]
                 }),
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(CountryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['meta_description'].widget.attrs['rows'] = 2
        form.base_fields['meta_description'].widget.attrs['cols'] = 10  # doesn't work...
        return form
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_group', 'hex', 'rgb', 'cmyk')
    search_fields = ['hex', 'rgb']
    list_filter = ['color_group']


class FlagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'is_published')
    search_fields = ['title']
    readonly_fields = ['updated_date', 'created_date']
    filter_horizontal = ('colors',)
    fieldsets = [
        (None, {
                'fields': [
                    'country', 'title', 'slug', 'name', 'date', 'proportion',
                    'colors', 'figure', 'emoji', 'short_description',
                    ]
                }),
        ('SEO', {
                'fields': [
                    'meta_title', 'meta_description', 'meta_keywords',
                    'meta_h1', 'is_published', 'is_index', 'is_follow',
                    'created_date', 'updated_date',
                    ]
                }),
    ]

    def get_form(self, request, obj=None, **kwargs):
        form = super(FlagAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['meta_description'].widget.attrs['rows'] = 2
        form.base_fields['meta_description'].widget.attrs['cols'] = 10  # doesn't work...
        return form
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


admin.site.register(Country, CountryAdmin)
admin.site.register(Flag, FlagAdmin)
admin.site.register(Color, ColorAdmin)
