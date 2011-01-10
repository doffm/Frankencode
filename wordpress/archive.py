import datetime
import time

from django.template import loader, RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response

from enginemodels import *

def filter_year (query, date_field, year):
    begin = datetime.datetime (year.year, 1, 1)
    end = datetime.datetime (year.year, 12, 31, 23, 59, 59)

    query.filter (date_field+' >=', begin)
    query.filter (date_field+' <=', end)
    
    return query

def filter_month (query, date_field, month):
    if month.month == 12:
        next_month = 1
        next_year = month.year + 1
    else:
        next_month = month.month + 1
        next_year = month.year

    begin = datetime.datetime (month.year, month.month, 1)
    
    next = datetime.datetime (next_year, next_month, 1)
    delta = datetime.timedelta (seconds=1)
    
    end = next - delta
    
    query.filter (date_field+' >=', begin)
    query.filter (date_field+' <=', end)
    
    return query

def filter_day (query, date_field, month):

    begin = datetime (day.year, day.month, day.day)
    end = datetime (day.year, day.month, day.day, 23, 59, 59)
    
    query.filter (date_field+' >=', begin)
    query.filter (date_field+' <=', end)
    
    return query

# --------------------  

def __load_and_respond (request, context, template_name,
                        template_loader=loader, extra_context=None, context_processors=None, mimetype=None):

    c = RequestContext(request, context, context_processors)

    if extra_context is None: extra_context = {}

    t = template_loader.get_template(template_name)

    for key, value in extra_context.items():
        if callable(value):
            c[key] = value()
        else:
            c[key] = value
    return HttpResponse(t.render(c), mimetype=mimetype)

# --------------------  

def archive_in_month (request, template_name, year, month,
                      template_loader=loader, extra_context=None, context_processors=None, mimetype=None):
    firstday = datetime.datetime (int(year), int(month), 1);

    queryset = wp_posts.all().filter ('post_status =', 'publish')
    queryset.order ('post_date_gmt')
    filter_month (queryset, 'post_date_gmt', firstday)

    return __load_and_respond (request, {'date':firstday, 'post_list':list(queryset)},
                               template_name, template_loader, extra_context, context_processors, mimetype)

def archive_in_day (request, template_name, year, month, day,
                    template_loader=loader, extra_context=None, context_processors=None, mimetype=None):
    day = datetime.datetime (int(year), int(month), int(day));

    queryset = wp_posts.all().filter ('post_status =', 'publish')
    queryset.order ('post_date_gmt')
    filter_day (queryset, 'post_date_gmt', day)

    return __load_and_respond (request, {'day':day, 'post_list':list(queryset)},
                               template_name, template_loader, extra_context, context_processors, mimetype)

# --------------------   

def split_on (ls, split):
    """
    Generator - Split a list in to groups.
    
    arg - ls: The list to split
    arg - split: A function that determines when two ajacent elements split the list
    """
    group = []
    while (len (ls) > 1):
        group.append (ls.pop(0))
        if split (group[-1], ls[0]):
            yield group
            group = []
    
    group += ls

    if len (group) == 0:
        return
    else:
        yield group

# --------------------
        
def year_groups (queryset):
    
    archive = queryset.order('-post_date_gmt')

    def new_year (a, b):
        if a.post_date_gmt.year != b.post_date_gmt.year:
            return True
        else:
            return False
    
    grouped_archive = split_on (list(archive), new_year)
    
    return [(year_group[0].post_date_gmt, year_group) for year_group in grouped_archive]


def month_groups (queryset, year):
    archive = filter_year (queryset, 'post_date_gmt', datetime.datetime (int(year), 1, 1))
    archive.order ('-post_date_gmt')
 
    def new_month (a, b):
        if a.post_date_gmt.month != b.post_date_gmt.month:
            return True
        else:
            return False
    
    grouped_archive = split_on (list(archive), new_month)
    
    return [(month_group[0].post_date_gmt, month_group) for month_group in grouped_archive]

def grouped_archive_by_year (request, template_name,
                             template_loader=loader, extra_context=None, context_processors=None, mimetype=None):
    queryset = wp_posts.all().filter ('post_status =', 'publish')
    date_groups = year_groups (queryset)
    return __load_and_respond (request, {'date_groups':date_groups},
                               template_name, template_loader, extra_context, context_processors, mimetype)

def grouped_archive_by_month (request, template_name, year,
                              template_loader=loader, extra_context=None, context_processors=None, mimetype=None):
    queryset = wp_posts.all().filter ('post_status =', 'publish')
    date_groups = month_groups (queryset, year)
    return __load_and_respond (request, {'date_groups':date_groups},
                               template_name, template_loader, extra_context, context_processors, mimetype)
