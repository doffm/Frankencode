from django.template import Context, RequestContext
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.cache import cache_page

from archive import grouped_archive_by_year, grouped_archive_by_month, archive_in_month, archive_in_day
from enginemodels import *

import time
import datetime
import re
 
@cache_page(60 * 60)
def object_detail(request, year, month, day, slug):
    try:
        tt = time.strptime('%s-%s-%s' % (year, month, day), '%s-%s-%s' % ('%Y', '%m', '%d'))
        date = datetime.date(*tt[:3])
    except ValueError:
        raise Http404
    
    query = wp_posts.all().filter ('post_status =', 'publish')
    #Filter on the day.
    query.filter ('post_date_gmt >=', datetime.datetime.combine (date, datetime.time.min))
    query.filter ('post_date_gmt <=', datetime.datetime.combine (date, datetime.time.max))
    #Filter on the slug.
    query.filter ('post_name =', slug)
    #Get the first in query
    post = query.get()
    
    comments = wp_comments.all().filter ('comment_post_id =', post.key().id())
    
    postIsHtml = False
    if (post.post_content.startswith('<p>') or post.post_content.startswith('<div>')):
        postIsHtml = True
    
    return render_to_response ('wordpress/post_detail.html', context_instance = RequestContext(request, {'post': post,
                                                                                                         'comments':comments,
                                                                                                         'post_is_html':postIsHtml}))

def archive_day(request, year, month, day):
    return archive_in_day (request, template_name='wordpress/post_archive_day.html', year=year, month=month, day=day)

def archive_month(request, year, month):
    return archive_in_month (request, template_name='wordpress/post_archive_month.html', year=year, month=month)

def archive_year(request, year):
    return grouped_archive_by_month (request, template_name='wordpress/post_archive_year.html', year=year)

@cache_page(60 * 60)
def archive_index(request):
    p = request.GET.get('p', None)
    if p:
        post = wp_posts.all().filter('__key__ =', int(p))
        if post:
            return HttpResponseRedirect(post.get_absolute_url())
        else:
            raise Http404
    return grouped_archive_by_year (request, template_name='wordpress/post_archive.html')
