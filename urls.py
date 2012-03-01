from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api/gallery/(?P<gallery_id>\d+)/$', 'api.views.gallery'),
)

urlpatterns += patterns('portfolio.views',
    url(r'^$', 'main', name='main'),
    url(r'^gallery/(?P<gallery_id>\d+)/$', 'gallery', name='gallery'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
