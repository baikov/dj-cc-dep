from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    list_filter = ['name']
    search_fields = ['name']
    # fieldsets = [
    #     (None, {'fields': ['is_published', 'title', 'is_highlighted', 'is_toc', 'toc_depth', 'short_text', 'image', 'body']}),
    #     ('SEO', {'fields': ['slug', 'seo_title', 'seo_description']}),
    # ]

admin.site.register(Country, CountryAdmin)
