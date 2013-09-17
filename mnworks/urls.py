from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'mnworks.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'mnworks.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)