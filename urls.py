from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^uploadify/', include('uploadify.urls')),
    url(r'^tinymce/filebrowser/', include('filebrowser.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^api/gallery/(?P<gallery_id>\d+)/$', 'api.views.gallery'),
)

urlpatterns += patterns('portfolio.views',
    url(r'^$', 'main', name='main'),
    url(r'^upload/$', 'upload_file', name='upload_file'),
    url(r'^gallery/(?P<gallery_id>\d+)/$', 'gallery', name='gallery'),
)

urlpatterns += patterns('blog.views',
    url(r'^blog/$', 'blog', name='blog'),
    url(r'^full_news/(?P<article_slug>\w+)/$', 'full_news', name='full_news'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
