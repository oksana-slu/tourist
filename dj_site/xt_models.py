
# in xtclass app
class XtC2C(models.Model):
    c2c_parent = models.IntegerField()
    c2c_child = models.IntegerField()
    class Meta:
        db_table = u'xt_c2c'

# in xtclass app
class XtClass(models.Model):
    nid = models.IntegerField(primary_key=True)
    vname = models.CharField(max_length=264)
    vcode = models.CharField(max_length=264)
    xtcdescription = models.CharField(max_length=240)
    nclasstype = models.IntegerField()
    nshablon = models.IntegerField()
    xtcconst = models.CharField(max_length=90)
    class_order = models.IntegerField()
    class Meta:
        db_table = u'xt_class'

# in xtclass app
class XtClasstype(models.Model):
    id = models.IntegerField(primary_key=True)
    nme = models.CharField(max_length=66)
    xtct_desc = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'xt_classtype'


class XtC2O(models.Model):
    nclass = models.IntegerField()
    nclassmain = models.IntegerField()
    nobj = models.IntegerField()
    class Meta:
        db_table = u'xt_c2o'

class XtLink(models.Model):
    link_id = models.IntegerField(primary_key=True)
    link = models.CharField(max_length=300)
    link_text = models.CharField(max_length=300, blank=True)
    link_desc = models.TextField(blank=True)
    link_author_id = models.IntegerField()
    link_isdirect = models.IntegerField()
    link_sort = models.IntegerField()
    class Meta:
        db_table = u'xt_link'

class XtNews(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(unique=True, max_length=264)
    title = models.TextField()
    description = models.TextField()
    author_id = models.IntegerField()
    date = models.IntegerField()
    forum = models.IntegerField()
    class Meta:
        db_table = u'xt_news'

class XtObject(models.Model):
    susid = models.IntegerField()
    status = models.IntegerField()
    freeedit = models.IntegerField()
    sustype = models.IntegerField()
    objid = models.IntegerField()
    objurl = models.CharField(max_length=240)
    susshabl = models.IntegerField()
    objfavour = models.BigIntegerField()
    view = models.IntegerField(null=True, blank=True)
    comment = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'xt_object'

class XtObjtype(models.Model):
    otid = models.IntegerField(primary_key=True)
    otname = models.CharField(max_length=66)
    ot_table_name = models.CharField(max_length=60)
    class Meta:
        db_table = u'xt_objtype'

class XtTemplates(models.Model):
    tmpid = models.IntegerField(primary_key=True)
    tmppath = models.CharField(max_length=240)
    tmptype = models.IntegerField()
    class Meta:
        db_table = u'xt_templates'

class XtTopic(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=264, blank=True)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    author_id = models.IntegerField()
    date = models.CharField(max_length=60, blank=True)
    forum = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'xt_topic'

class Xtplace(models.Model):
    id = models.IntegerField()
    nparent = models.IntegerField(null=True, blank=True)
    ntype = models.IntegerField(null=True, blank=True)
    vname = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'xtplace'

class Xtplacetype(models.Model):
    id = models.IntegerField(null=True, blank=True)
    vname = models.CharField(max_length=108, blank=True)
    class Meta:
        db_table = u'xtplacetype'

