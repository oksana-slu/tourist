from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic
from dj_site.xtobject.models import XtObject


def index(request):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')

    latest_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                          status=1).order_by('-pk')[0:6]
    top_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                       status=1).order_by('-comment')[0:6]

    recent_report = XtObject.objects.filter(xtobjecttype__otname='report',
                                            status=1).order_by('-pk')[0:6]
    popular_report = XtObject.objects.filter(xtobjecttype__otname='report',
                                             status=1).order_by('-comment')[0:6]

    new_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                           status=1).order_by('-pk')[0:6]
    best_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                           status=1).order_by('-comment')[0:6]


    return render_to_response('index.html', {"napr_xt_classes": napr_xt_classes,
                                             "geogr_xt_classes": geogr_xt_classes,
                                             "latest_news": latest_news,
                                             "top_news": top_news,
                                             "recent_report": recent_report,
                                             "popular_report": popular_report,
                                             "new_article": new_article,
                                             "best_article": best_article},
                              context_instance=RequestContext(request))


def xtreport_list(request, part):
    return render_to_response('repo_list.html', {},
                              context_instance=RequestContext(request))


def xttopic_item(request, part, slug):
    object_item = XtObject.objects.get(objurl='%s/%s' %(part, slug))
    topic_item = object_item.content_object

    latest_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                          status=1).exclude(id=object_item.id).order_by('-pk')[0:6]

    top_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                       status=1).exclude(id=object_item.id).order_by('-comment')[0:6]

    recent_report =XtObject.objects.filter(xtobjecttype__otname='report',
                                           status=1).exclude(id=object_item.id).order_by('-pk')[0:6]

    popular_report = XtObject.objects.filter(xtobjecttype__otname='report',
                                             status=1).exclude(id=object_item.id).order_by('-comment')[0:6]

    new_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                          status=1).exclude(id=object_item.id).order_by('-pk')[0:6]

    best_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                           status=1).exclude(id=object_item.id).order_by('-comment')[0:6]

    return render_to_response('repo.html', {"object_item": object_item,
                                            "topic_item": topic_item,
                                            "latest_news": latest_news,
                                            "top_news": top_news,
                                            "part": part,
                                            "recent_report": recent_report,
                                            "popular_report": popular_report,
                                            "new_article": new_article,
                                            "best_article": best_article},
                              context_instance=RequestContext(request))


def xtclass(request, slug):
    xtcdescription_xtclass = XtClass.objects.get(vcode=slug)

    latest_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                          status=1,
                                          xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]
    top_news = XtObject.objects.filter(xtobjecttype__otname='news',
                                       status=1,
                                       xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]

    recent_report =XtObject.objects.filter(xtobjecttype__otname='report',
                                           status=1,
                                           xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]

    popular_report = XtObject.objects.filter(xtobjecttype__otname='report',
                                             status=1,
                                             xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]

    new_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                          status=1,
                                          xtc2o__xtclass__vcode=slug).order_by('-pk')[0:6]

    best_article = XtObject.objects.filter(xtobjecttype__otname='article',
                                           status=1,
                                           xtc2o__xtclass__vcode=slug).order_by('-comment')[0:6]

    return render_to_response('class.html', {"xtcdescription_xtclass": xtcdescription_xtclass,
                                             "top_news": top_news,
                                             "latest_news": latest_news,
                                             "recent_report": recent_report,
                                             "popular_report": popular_report,
                                             "new_article": new_article,
                                             "best_article": best_article},
                              context_instance=RequestContext(request))
