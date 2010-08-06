from django.db import models


class XtClasstype(models.Model):
    id = models.IntegerField(primary_key=True)
    nme = models.CharField(max_length=66, unique=True)
    xtct_desc = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return self.nme

    class Meta:
        db_table = u'xt_classtype'


class XtClass(models.Model):
    nid = models.IntegerField(primary_key=True)
    vname = models.CharField(max_length=264)
    vcode = models.CharField(max_length=264)
    xtcdescription = models.CharField(max_length=240, blank=True)
    xtclasstype = models.ForeignKey(XtClasstype, db_column='nclasstype')
    nshablon = models.IntegerField(null=True, blank=True)
    xtcconst = models.CharField(max_length=90, blank=True)
    class_order = models.IntegerField(default=0)

    class Meta:
        db_table = u'xt_class'

    def __unicode__(self):
        return self.vcode

    def get_childs(self):
        return self.parents.select_related('child').all().order_by("-child__class_order")


class XtC2C(models.Model):
    parent = models.ForeignKey(XtClass, db_column='c2c_parent', related_name='parents')
    child = models.ForeignKey(XtClass, db_column='c2c_child', related_name='childs')

    class Meta:
        db_table = u'xt_c2c'
        unique_together = (("parent", "child"), )

