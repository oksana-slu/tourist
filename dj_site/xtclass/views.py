from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic
from dj_site.xtobject.models import XtObject



def xtclass(request, slug):
    xtcdescription_xtclass = XtClass.objects.get(vcode=slug)

    latest_news = XtObject.news.filter(xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]
    top_news = XtObject.news.filter(xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]

    recent_report =XtObject.report.filter(xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]
    popular_report = XtObject.report.filter(xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]

    new_article = XtObject.article.filter(xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]
    best_article = XtObject.article.filter(xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]
    
    link = XtObject.link.filter(xtc2o__xtclass__vcode=slug)

    return render_to_response('class.html', {"xtcdescription_xtclass": xtcdescription_xtclass,
                                             "top_news": top_news,
                                             "latest_news": latest_news,
                                             "recent_report": recent_report,
                                             "popular_report": popular_report,
                                             "new_article": new_article,
                                             "best_article": best_article,
                                             "link": link},
                              context_instance=RequestContext(request))