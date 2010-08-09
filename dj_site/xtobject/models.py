from django.db import models
from dj_site.xtclass.models import XtClass


class XtObjecttype(models.Model):
    id = models.IntegerField(primary_key=True, db_column='otid')
    otname = models.CharField(max_length=66, blank=True)
    ot_table_name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.otname

    class Meta:
        db_table = u'xt_objtype'


class XtObject(models.Model):
    id = models.IntegerField(primary_key=True, db_column='susid')
    status = models.IntegerField(default=3)
    freeedit = models.IntegerField(default=0)
    xtobjecttype = models.ForeignKey(XtObjecttype, db_column='sustype')
    objid = models.IntegerField()
    objurl = models.CharField(max_length=240, blank=True)
    susshabl = models.IntegerField(default=0)
    objfavour = models.BigIntegerField(default=0)
    view = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return u'%d - %d' % (self.id, self.objid)

    class Meta:
        db_table = u'xt_object'


class XtC2O(models.Model):
    xtclass = models.ForeignKey(XtClass, db_column='nclass')
    nclassmain = models.IntegerField()
    xtobject = models.ForeignKey(XtObject, db_column='nobj')

    class Meta:
        db_table = u'xt_c2o'
