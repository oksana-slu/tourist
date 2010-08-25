from django.db import models
from datetime import date


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
        
    def dateformat(self):
        print self.date
        d = date.fromtimestamp(self.date)
        print d 
        return d    
        
    class Meta:
        abstract = True


class XtNews(XtTopicAbstract):    
    
    class Meta:
        db_table = u'xt_news'


class XtTopic(XtTopicAbstract):

    class Meta:
        db_table = u'xt_topic'
