from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^nevermatter/exhibit/(?P<exhibit_id>\d+)/$', 'nevermatter.gallery.views.exhibit'),
    (r'^nevermatter/$', 'nevermatter.gallery.views.overview'),
    (r'^admin/(.*)', admin.site.root),
)

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/Users/domcrayford/Documents/Dev/nevermatter/media', 'show_indexes':True}),
    )
    
