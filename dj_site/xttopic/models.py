import os
from datetime import date
from lxml import etree

from django.db import models

from django.conf import settings


class XtTopicAbstract(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(blank=True, max_length=264)
    title = models.TextField()
    description = models.TextField()
    author_id = models.IntegerField()
    date = models.IntegerField()
    forum = models.IntegerField()

    def __unicode__(self):
        return self.title

    class Meta:
        abstract = True

    def dateformat(self):
        return date.fromtimestamp(long(self.date))
        
    def get_text(self):
        file_name = os.path.join(settings.MEDIA_ROOT, self.path, 'topic.xml')
        text = ''
        if os.path.isfile(file_name):
            fp = open(file_name, 'r')
            file_text = fp.read()
            if file_text:
                root_tree = etree.XML(file_text)
                text = root_tree.find('sheet/text').text

        if not text:
            text = "Text is empty"
        return text
        
    def get_ico_url(self):
        url_name = '/' + self.path + 'ico.jpg'
        return url_name


class XtNews(XtTopicAbstract):

    class Meta:
        db_table = u'xt_news'


class XtTopic(XtTopicAbstract):

    class Meta:
        db_table = u'xt_topic'
