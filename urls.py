from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^exhibit/(?P<exhibit_id>\d+)/$', 'nevermatter.gallery.views.exhibit'),
    (r'^contact/$', 'nevermatter.gallery.views.contact'),
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'nevermatter.gallery.views.overview'),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/domcrayford/Documents/Dev/nevermatter_static', 'show_indexes':True}),
    )
    
