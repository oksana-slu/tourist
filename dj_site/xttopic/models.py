from django.db import models
from datetime import date
from dj_site.settings import MEDIA_ROOT
import os


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
        
    def text(self):
        t = os.path.join(MEDIA_ROOT, self.path, 'topic.xml')
        fp = open(t, 'r')
        return fp.read()
        

class XtNews(XtTopicAbstract):

    class Meta:
        db_table = u'xt_news'


class XtTopic(XtTopicAbstract):

    class Meta:
        db_table = u'xt_topic'
