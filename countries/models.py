from django.db import models

class Country (models.Model):

    class Continents(models.TextChoices):  	  	  	  	  	  
        AFRICA = 'AF', _('Африка')
        ASIA = 'AS', _('Евразия')
        EUROPE = 'EU', _('Евразия')
        NORTH_AMERICA = 'NA', _('Северная Америка')
        SOUTH_AMERICA = 'SA', _('Южная Америка')
        AUSTRALIA = 'AU', _('Австралия')
        EMPTY = 'NO', _('')

    name = models.CharField(verbose_name='Название', max_length=250)
    conventional_long_name = models.CharField(verbose_name='Официальное название', max_length=250)
    local_long_name = models.CharField(verbose_name='Официальное название на местном языке', max_length=250, blank=True)
    local_short_name = models.CharField(verbose_name='Короткое название на местном языке', max_length=250, blank=True)
    capital_name = models.CharField(verbose_name='Столица', max_length=250, blank=True)
    continent = models.CharField(verbose_name='Континент', 
                                choices=Continents.choices,
                                default=Continents.EMPTY,
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
