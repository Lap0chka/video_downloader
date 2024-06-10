from django import template

register = template.Library()


@register.filter
def custom_split(value):
    try:
        return value.split('-')
    except IndexError:
        return value
