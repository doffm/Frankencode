from django import template

from frankfeeds.latestblog import getBlog

register = template.Library()

@register.inclusion_tag ('latestblog.html')
def latestblog ():
    latest = getBlog ()

    return {'title':latest.title, 'summary':latest.summary}
