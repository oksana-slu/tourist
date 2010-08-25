from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from dj_site.xtclass.models import XtClass


class XtObjecttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='otid')
    otname = models.CharField(max_length=66, blank=True)
    ot_table_name = models.CharField(max_length=60)

    def __unicode__(self):
        return u'%s' % self.otname

    class Meta:
        db_table = u'xt_objtype'


class NewsManager(models.Manager):

    def get_query_set(self):
        return super(NewsManager, self).get_query_set().filter(xtobjecttype__otname='news', status=1)


class ReportManager(models.Manager):

    def get_query_set(self):
        return super(ReportManager, self).get_query_set().filter(xtobjecttype__otname='report', status=1)


class ArticleManager(models.Manager):

    def get_query_set(self):
        return super(ArticleManager, self).get_query_set().filter(xtobjecttype__otname='article', status=1)


class XtObject(models.Model):
    id = models.IntegerField(primary_key=True, db_column='susid')
    status = models.IntegerField(default=3)
    freeedit = models.IntegerField(default=0)

    xtobjecttype = models.ForeignKey(XtObjecttype, db_column='sustype')

    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in': ('xtlink', 'xtnews', 'xttopic')})
    object_id = models.PositiveIntegerField(db_column='objid')
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objurl = models.CharField(max_length=240, blank=True)
    susshabl = models.IntegerField(default=0)
    objfavour = models.BigIntegerField(default=0)
    view = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField(null=True, blank=True)

    objects = models.Manager()
    news = NewsManager()
    report = ReportManager()
    article = ArticleManager()

    def __unicode__(self):
        return u'%d - %d' % (self.id, self.object_id)

    def xtclass(self):
        return self.xtc2o_set.all()

    class Meta:
        db_table = u'xt_object'


class XtC2O(models.Model):
    xtclass = models.ForeignKey(XtClass, db_column='nclass')
    nclassmain = models.IntegerField()
    xtobject = models.ForeignKey(XtObject, db_column='nobj')

    class Meta:
        db_table = u'xt_c2o'
