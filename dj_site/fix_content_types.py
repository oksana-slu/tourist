from dj_site.xtobject.models import XtObject
from django.contrib.contenttypes.models import ContentType
topic = ContentType.objects.get(model='xttopic')
XtObject.objects.filter(xtobjecttype__pk__in = (1, 2)).update(content_type=topic)
link = ContentType.objects.get(model='xtlink')
XtObject.objects.filter(xtobjecttype__pk = 3).update(content_type=link)
news = ContentType.objects.get(model='xtnews')
XtObject.objects.filter(xtobjecttype__pk = 5).update(content_type=news)
