import os

from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', "dj_site.views.index"),
    (r'^edit_link$', "dj_site.xtlink.views.edit_link"),
    (r'^edit_link/(?P<link_id>\d+)$', "dj_site.xtlink.views.edit_link"),
    (r'^add_news/$', "dj_site.xttopic.views.add_news"),
    (r'^(?P<part>add_report|add_article)/$', "dj_site.xttopic.views.add_topic"),
    (r'^edit_news/(?P<news_id>\d+)$', "dj_site.xttopic.views.edit_news"),
    (r'^(?P<part>edit_report|edit_article)/(?P<topic_id>\d+)$', "dj_site.xttopic.views.edit_topic"),
    (r'^upload_ico/(?P<part>[-\w]+)/(?P<news_id>\d+)$', "dj_site.xttopic.views.upload_ico"),
    (r'^(?P<part>xtreport|xtarticle|xtnews)/(?P<slug>[-\w]+)$', "dj_site.xttopic.views.xttopic_item"),
    (r'^(?P<part>xtreport|xtarticle|xtnews)/(?P<slug>[-\w]+)/(?P<sheet_number>\d+)$', "dj_site.xttopic.views.xttopic_item"),
    (r'^(?P<part>xtreport|xtarticle|xtnews)/$', "dj_site.views.xtreport_list"),
    (r'^xtclass/(?P<slug>[-\w]+)$', "dj_site.xtclass.views.xtclass"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        (r'^news/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.MEDIA_ROOT, 'news')}),
        (r'^article/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.MEDIA_ROOT, 'article')}),
        (r'^report/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(settings.MEDIA_ROOT, 'report')}),
    )
