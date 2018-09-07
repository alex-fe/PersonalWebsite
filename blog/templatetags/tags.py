from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def deslugify(string):
    return string.replace('-', ' ')


@register.filter
@stringfilter
def blurb(string):
    cutoff = 200
    try:
        i = string.index('<')
    except ValueError:
        return string[:cutoff]
    else:
        i = i if i < cutoff else cutoff
        return string[:i]
