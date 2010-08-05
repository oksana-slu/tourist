from django.db import models
       
             
        
class XtClasstype(models.Model):
    id = models.IntegerField(primary_key=True)
    nme = models.CharField(max_length=66)
    xtct_desc = models.CharField(max_length=300, blank=True)
    def __unicode__(self):
        return self.nme
    class Meta:
        db_table = u'xt_classtype'
       
       

class XtClass(models.Model):
    nid = models.IntegerField(primary_key=True)
    vname = models.CharField(max_length=264)
    vcode = models.CharField(max_length=264)
    xtcdescription = models.CharField(max_length=240)
    xtclasstype = models.ForeignKey(XtClasstype, db_column='nclasstype')
    nshablon = models.IntegerField()
    xtcconst = models.CharField(max_length=90)
    class_order = models.IntegerField()
    def __unicode__(self):
        return self.vcode
    
    class Meta:
        db_table = u'xt_class'
        
        
class XtC2C(models.Model):
    parent = models.ForeignKey(XtClass, db_column='c2c_parent', related_name='parent')
    child = models.ForeignKey(XtClass, db_column='c2c_child', related_name='child')
    
    class Meta:
        db_table = u'xt_c2c'
        unique_together = (("parent", "child"),)