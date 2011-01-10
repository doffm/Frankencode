import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='remove_newlines')
@stringfilter
def remove_newlines(value):
    return re.sub ('([\r\n]{1})[\r\n]+', '\n\n', value.lstrip())
remove_newlines.is_safe = True
        
@register.filter(name='empty_paragraphs')
@stringfilter
def empty_paragraphs(value):
    return re.sub ('<p>\s*</p>', '', value)
empty_paragraphs.is_safe = True
