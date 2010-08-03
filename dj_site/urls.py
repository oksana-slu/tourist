from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "dj_site.views.index"),
    (r'^(xtreport|xtarticle|xtnews)/$', "dj_site.views.xtreport_list"),
    (r'^(xtreport|xtarticle|xtnews)/(?P<slug>[-\w]+)$', "dj_site.views.xtreport_item"),
    (r'^xtclass/(?P<slug>[-\w]+)$', "dj_site.views.xtclass"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
