from django import template

register = template.Library()


@register.filter()
def get_name(object, field):
    verbose_name = object._meta.get_field(field).verbose_name
    return verbose_name
