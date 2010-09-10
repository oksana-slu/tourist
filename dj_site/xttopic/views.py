from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic
from dj_site.xtobject.models import XtObject


def xttopic_item(request, part, slug, sheet_number=1):
    object_item = XtObject.objects.get(objurl='%s/%s' %(part, slug))
    topic_item = object_item.content_object
    sheet_number = int(sheet_number)
    topic_text = topic_item.get_text(sheet_number)
    sheets_count = topic_item.get_sheets_count()
    sheets_range = range(1, sheets_count + 1)

    latest_news = XtObject.news.exclude(id=object_item.id).order_by('-pk')[0:6]
    top_news = XtObject.news.exclude(id=object_item.id).order_by('-comment')[0:6]

    recent_report =XtObject.report.exclude(id=object_item.id).order_by('-pk')[0:6]
    popular_report = XtObject.report.exclude(id=object_item.id).order_by('-comment')[0:6]

    new_article = XtObject.article.exclude(id=object_item.id).order_by('-pk')[0:6]
    best_article = XtObject.article.exclude(id=object_item.id).order_by('-comment')[0:6]

    return render_to_response('repo.html', {"object_item": object_item,
                                            "topic_item": topic_item,
                                            "topic_text": topic_text,
                                            "sheets_range": sheets_range,
                                            "sheet_number": sheet_number,
                                            "sheets_count": sheets_count,
                                            "latest_news": latest_news,
                                            "top_news": top_news,
                                            "part": part,
                                            "slug":slug,
                                            "recent_report": recent_report,
                                            "popular_report": popular_report,
                                            "new_article": new_article,
                                            "best_article": best_article},
                              context_instance=RequestContext(request))