from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError

from utils.color import Colorize


class Seo (models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=100, unique=True,)
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


class CustomQuerySet(models.QuerySet):
    def published(self):
        return self.filter(is_published=True)

    # def featured(self):
    #     return self.filter(is_highlighted=True)


class Country (Seo, models.Model):

    class Continents (models.TextChoices):
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
    continent = models.CharField(verbose_name='Континент', choices=Continents.choices, default=Continents.EMPTY,
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

    objects = CustomQuerySet.as_manager()

    def __str__(self):
        return self.name


class Color(models.Model):

    class Colors(models.TextChoices):
        RED = 'red', 'Красный'
        ORANGE = 'orange', 'Оранжевый'
        YELLOW = 'yellow', 'Желтый'
        GREEN = 'green', 'Зеленый'
        BLUE = 'blue', 'Синий'
        PURPLE = 'purple', 'Фиолетовый'
        BLACK = 'black', 'Черный'
        BROWN = 'brown', 'Коричневый'
        MAROON = 'maroon', 'Бордовый'
        PINK = 'pink', 'Розовый'
        WHITE = 'white', 'Белый'
        EMPTY = 'NO', ''
    # name = models.CharField(verbose_name='Название', max_length=250)
    color_group = models.CharField(verbose_name='Группа цветов', choices=Colors.choices,
                                   default=Colors.EMPTY, max_length=50,)
    hex = models.CharField(verbose_name='HEX', max_length=7, unique=True, blank=True)
    rgb = ArrayField(models.SmallIntegerField(), blank=True, size=3, verbose_name='RGB')
    cmyk = ArrayField(models.SmallIntegerField(), blank=True, size=4, verbose_name='CMYK')
    pantone = models.CharField(verbose_name='Pantone', max_length=100, blank=True)

    def save(self, *args, **kwargs):

        if self.cmyk:
            color = Colorize(cmyk=self.cmyk)

        if self.hex:
            color = Colorize(hex=self.hex)

        if self.rgb:
            color = Colorize(self.rgb)

        self.hex = color.hex
        self.rgb = color.rgb
        self.cmyk = color.cmyk

        super(Color, self).save(*args, **kwargs)

    def clean(self):
        if not self.rgb and not self.hex and not self.cmyk:
            raise ValidationError({'rgb': 'Одно из полей должно быть заполнено'})

    def __str__(self):
        return f'{self.color_group}: #{self.hex}'


class Flag(Seo, models.Model):

    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='flags')
    title = models.CharField(verbose_name='Заголовок', max_length=250)
    name = models.CharField(verbose_name='Название', max_length=250, blank=True)
    date = models.DateField(verbose_name='Дата утверждения', blank=True,)
    # use_for = models.CharField(verbose_name='Название', max_length=250, blank=True)
    proportion = models.CharField(verbose_name='Пропорции', max_length=10, blank=True)
    emoji = models.CharField(verbose_name='Эмоджи', max_length=20, blank=True)
    short_description = models.TextField(max_length=550, verbose_name='Краткое описание', blank=True)
    colors = models.ManyToManyField(Color, related_name='flags', verbose_name='Цвета', blank=True)
    flag_day = models.DateField(verbose_name='День флага', blank=True,)

    # Characteristics
    is_horizontal_stripes = models.BooleanField(verbose_name='Горизонтальные полосы', default=False)
    is_vertical_stripes = models.BooleanField(verbose_name='Вертикальные полосы', default=False)
    is_diagonal_stripes = models.BooleanField(verbose_name='Диагональные полосы', default=False)
    is_motto = models.BooleanField(verbose_name='Девиз', default=False)
    is_country_name = models.BooleanField(verbose_name='Название страны', default=False)
    is_crescent = models.BooleanField(verbose_name='Полумесяц', default=False)
    is_star = models.BooleanField(verbose_name='Звезда', default=False)
    is_emblem = models.BooleanField(verbose_name='Герб', default=False)
    is_animal = models.BooleanField(verbose_name='Животное', default=False)
    is_bird = models.BooleanField(verbose_name='Птица', default=False)
    is_crown = models.BooleanField(verbose_name='Корона', default=False)
    is_weapon = models.BooleanField(verbose_name='Оружие', default=False)
    is_sun = models.BooleanField(verbose_name='Солнце', default=False)
    is_plant = models.BooleanField(verbose_name='Растение', default=False)
    is_circle = models.BooleanField(verbose_name='Круг', default=False)
    is_triangle = models.BooleanField(verbose_name='Треугольник', default=False)
    is_cross = models.BooleanField(verbose_name='Крест', default=False)
    is_diamond = models.BooleanField(verbose_name='Ромб', default=False)

    objects = CustomQuerySet.as_manager()

    def __str__(self):
        return self.title
