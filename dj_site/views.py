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
                                             
    latest_news = XtNews.objects.all().order_by('-date')[0:6]
    top_news = XtNews.objects.all().order_by('-forum')[0:6]
    
    recent_report = XtTopic.objects.filter(path__startswith='report').\
                                          order_by('-date')[0:6]
    popular_report = XtTopic.objects.filter(path__startswith='report').\
                                          order_by('-forum')[0:6]
                                          
    new_article = XtTopic.objects.filter(path__startswith='article').\
                                          order_by('-date')[0:6]
    best_article = XtTopic.objects.filter(path__startswith='article').\
                                          order_by('-forum')[0:6]


    return render_to_response('index.html', {"napr_xt_classes": napr_xt_classes,
                                             "geogr_xt_classes": geogr_xt_classes,
                                             "latest_news":latest_news,
                                             "top_news":top_news,
                                             "recent_report":recent_report,
                                             "popular_report":popular_report,
                                             "new_article":new_article,
                                             "best_article":best_article},
                              context_instance=RequestContext(request))


def xtreport_list(request, part):
    return render_to_response('repo_list.html', {},
                              context_instance=RequestContext(request))


def xtreport_item(request, part, slug):
    xt_all = XtObject.objects.get(objurl='%s/%s' %(part, slug))
    xtclass = xt_all.xtc2o_set.all()
    return render_to_response('repo.html', {"xtclass":xtclass},
                              context_instance=RequestContext(request))


def xtclass(request, slug):
    xtcdescription_xtclass = XtClass.objects.get(vcode=slug)
    return render_to_response('class.html', {"xtcdescription_xtclass": xtcdescription_xtclass},
                              context_instance=RequestContext(request))
