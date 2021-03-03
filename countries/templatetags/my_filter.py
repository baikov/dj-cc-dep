from django import template
from config.settings.base import MEDIA_URL

register = template.Library()


@register.filter()
def get_name(object, field):
    verbose_name = object._meta.get_field(field).verbose_name
    return verbose_name


@register.filter()
def in_km(field):
    width = f'{field/1000} км'
    return width


@register.filter()
def get_img_path(object, size):
    object = object.lower()
    return f'{MEDIA_URL}/national-flags/{object}/{size}/{object}'
