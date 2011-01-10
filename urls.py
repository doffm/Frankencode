from django.conf.urls.defaults import *
from django.views.generic.simple import *

import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns ('',
    # Example:
    # (r'^frankencode/', include('frankencode.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),


    ('^home$',     'views.home'),
    ('^hire$',     'views.hire'),
    ('^projects$', 'views.projects'),
    ('^resume$',   'views.resume'),
    ('^$', redirect_to, {'url': '/home'}),

    ('^index.php/', include('wordpress.urls')),
    ('^index.php', redirect_to, {'url': '/index.php/'}),
)

#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
#    )
#
#    urlpatterns += patterns('',
#        (r'^wp-content/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.WP_STATIC_ROOT}),
#    )
