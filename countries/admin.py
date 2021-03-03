from django.contrib import admin
from .models import BorderCountry, Country, Flag, Color, HistoricalFlag
from django.forms import TextInput
from django.db import models


class BorderCountryInline(admin.TabularInline):
    model = BorderCountry
    extra = 2
    fk_name = 'country'
    raw_id_fields = ('border_country',)


class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'iso_code_a2', 'slug', 'is_published',)
    # list_filter = ['name']
    search_fields = ['name', 'iso_code_a2']
    readonly_fields = ['updated_date', 'created_date']
    inlines = (BorderCountryInline,)
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'conventional_long_name', 'local_long_name', 'local_short_name',
                           'capital_name', 'continent', 'anthem', 'motto', 'official_language', 'national_language',
                           'internet_tld',
                           ]
                }),
        ('Данные о стране', {'fields': [
                ('iso_code_a2', 'iso_code_a3', 'iso_code_num'),
                ('currency_name', 'currency_code', 'currency_simbol'),
        ]}),
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


class HistoricalFlagAdmin(admin.ModelAdmin):
    list_display = ('from_year', 'to_year', 'country', 'title')
    search_fields = ['title', 'from_year', 'country__name']
    list_filter = ['country__name']
    raw_id_fields = ('country',)
    fieldsets = [
        (None, {
                'fields': [
                    'country', 'title', 'image_url', 'image_path',
                    ('from_year', 'to_year'),
                    'description'
                    ]
                }),
    ]


class FlagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'country', 'is_published')
    search_fields = ['title', 'country__name']
    list_filter = ['colors__color_group']
    raw_id_fields = ('country',)
    readonly_fields = ['updated_date', 'created_date']
    filter_horizontal = ('colors',)
    fieldsets = [
        (None, {
                'fields': [
                    'country', 'title', 'slug', 'name', 'date', 'flag_day', 'proportion',
                    'colors', 'emoji', 'short_description', 'construction_image', 'design_description',
                    'history_text', 'flag_facts', 'usage_description',
                    ]
                }),
        ('На флаге', {
                'classes': ('collapse', 'wide', 'extrapretty'),
                'fields': [
                    ('is_horizontal_stripes', 'is_vertical_stripes', 'is_diagonal_stripes'),
                    ('is_motto', 'is_country_name', 'is_emblem'),
                    ('is_crescent', 'is_star', 'is_animal', 'is_bird', 'is_crown', 'is_weapon', 'is_sun', 'is_plant'),
                    ('is_circle', 'is_triangle', 'is_cross', 'is_diamond')
                    ]
                }),
        ('SEO', {
                'classes': ('collapse', 'wide'),
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
admin.site.register(HistoricalFlag, HistoricalFlagAdmin)
