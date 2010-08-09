from django.db import models


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
