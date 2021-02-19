from django.db import models
from django.contrib.postgres.fields import ArrayField

class Seo (models.Model):
    class Meta:
        abstract = True
        
    meta_title = models.CharField(verbose_name='SEO Title', max_length=250, blank=True)
    meta_description = models.TextField(
        max_length=400, verbose_name='SEO Description', blank=True)
    meta_keywords = models.CharField(verbose_name='SEO keywords', max_length=250, blank=True)
    meta_h1 = models.CharField(verbose_name='SEO H1', max_length=250, blank=True)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False, null=False)
    # is_highlighted = models.BooleanField(verbose_name='Featured', default=False)
    is_index = models.BooleanField(verbose_name='index', default=True, null=False)
    is_follow = models.BooleanField(verbose_name='follow', default=True, null=False)
    # shemaorg_markup
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class Country (models.Model):

    class Continents(models.TextChoices):  	  	  	  	  	  
        AFRICA = 'AF', 'Африка'
        ASIA = 'AS', 'Евразия (Азия)'
        EUROPE = 'EU', 'Евразия (Европа)'
        NORTH_AMERICA = 'NA', 'Северная Америка'
        SOUTH_AMERICA = 'SA', 'Южная Америка'
        AUSTRALIA = 'AU', 'Австралия'
        EMPTY = 'NO', ''

    name = models.CharField(verbose_name='Название', max_length=250)
    conventional_long_name = models.CharField(verbose_name='Официальное название', max_length=250)
    local_long_name = models.CharField(verbose_name='Официальное название на местном языке', max_length=250, blank=True)
    local_short_name = models.CharField(verbose_name='Короткое название на местном языке', max_length=250, blank=True)
    capital_name = models.CharField(verbose_name='Столица', max_length=250, blank=True)
    continent = models.CharField(verbose_name='Континент', 
                                choices=Continents.choices,
                                default=Continents.EMPTY,
                                max_length=50,
                                )
    anthem = models.URLField(verbose_name='Гимн', max_length=250, blank=True)
    motto = models.CharField(verbose_name='Девиз', max_length=250, blank=True)
    official_language = models.CharField(verbose_name='Официальный язык', max_length=50, blank=True)
    national_language = models.CharField(verbose_name='Национальный язык', max_length=50, blank=True)
    internet_tld = models.CharField(verbose_name='Интернет-домен', max_length=10, blank=True)
    currency_name = models.CharField(verbose_name='Название валюты', max_length=50, blank=True)
    currency_code = models.CharField(verbose_name='Код валюты', max_length=3, blank=True)
    currency_simbol = models.CharField(verbose_name='Символ валюты', max_length=1, blank=True)
    iso_code_a2 = models.CharField(verbose_name='ISO код (2alpha)', max_length=2, blank=True)
    iso_code_a3 = models.CharField(verbose_name='ISO код (3alpha)', max_length=3, blank=True)
    iso_code_num = models.CharField(verbose_name='ISO код (numeric)', max_length=4, blank=True)

    slug = models.SlugField(max_length=100, unique=True,)

    def __str__(self):
        return self.name

class Flag(Seo, models.Model):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='flags')
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    slug = models.SlugField(max_length=100, unique=True,)
    name = models.CharField(verbose_name='Название', max_length=250, blank=True)
    date = models.DateField(verbose_name='Дата утверждения', blank=True,)
    # use_for = models.CharField(verbose_name='Название', max_length=250, blank=True)
    proportion = models.CharField(verbose_name='Пропорции', max_length=10, blank=True)
    colors = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    figure = models.CharField(verbose_name='Фигура на флаге', max_length=250, blank=True)
    emoji = models.CharField(verbose_name='Эмоджи', max_length=20, blank=True)
    short_description = models.TextField(
        max_length=550, verbose_name='Краткое описание', blank=True)

    def __str__(self):
        return self.title
