from django import template

register = template.Library()


@register.simple_tag
def ss_separator(value, delimiter, output='title'):
    if output == 'color':
        return str(value.split(delimiter)[1])
    return str(value.split(delimiter)[0])
