from django import template
from decimal import Decimal,DecimalException

register = template.Library()


@register.simple_tag
def ss_separator(value, delimiter, output='title'):
    if output == 'color':
        return str(value.split(delimiter)[1])
    return str(value.split(delimiter)[0])

@register.simple_tag
def round_decimal(value, decimal_places=6):
    try:
        return round(float(value), decimal_places)
    except (ValueError, TypeError):
        return value

@register.simple_tag
def format_scientific(value, decimal_places=3):
    try:
        decimal_value = Decimal(value)
        return "{:.{}E}".format(decimal_value, decimal_places)
    except (ValueError, TypeError, DecimalException):
        return value

@register.simple_tag
def lol(val):
    return 60