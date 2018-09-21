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
    """Shorten body of text to blub length.
    Args:
        string (str): Text to shorten.
    Returns:
        Abbreviated text.
    """
    cutoff = 200
    for tag in ('<', '!['):  # tags and markdown images
        try:
            i = string.index(tag)
        except ValueError:
            pass
        else:
            cutoff = i if i < cutoff else cutoff
    return string[:cutoff]
