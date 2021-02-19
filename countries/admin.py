from django.contrib import admin
from .models import Country, Flag
from django.forms import TextInput, Textarea
from django.db import models

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    list_filter = ['name']
    search_fields = ['name']
    # fieldsets = [
    #     (None, {'fields': ['is_published', 'title', 'is_highlighted', 'is_toc', 'toc_depth', 'short_text', 'image', 'body']}),
    #     ('SEO', {'fields': ['slug', 'seo_title', 'seo_description']}),
    # ]

class FlagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'colors')
    search_fields = ['title']
    readonly_fields = ['updated_date', 'created_date']
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
        form.base_fields['meta_description'].widget.attrs['cols'] = 10 # doesn't work...
        return form
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
    }

admin.site.register(Country, CountryAdmin)
admin.site.register(Flag, FlagAdmin)
