from django.db import models


class XtLink(models.Model):
    id = models.AutoField(primary_key=True, db_column='link_id')
    link = models.CharField(max_length=300)
    link_text = models.CharField(max_length=300, blank=True)
    link_desc = models.TextField(blank=True)
    link_author_id = models.IntegerField()
    link_isdirect = models.IntegerField(default=0)
    link_sort = models.IntegerField(default=0)

    def __unicode__(self):
        return self.link

    class Meta:
        db_table = u'xt_link'
