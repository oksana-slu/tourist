from dj_site.xtobject.models import XtObject
XtObject.objects.filter(xtobjecttype__pk__in = (1, 2)).update(content_type=17)
XtObject.objects.filter(xtobjecttype__pk = 3).update(content_type=15)
XtObject.objects.filter(xtobjecttype__pk = 5).update(content_type=16)
