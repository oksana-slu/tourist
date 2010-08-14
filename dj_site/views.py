from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic


def index(request):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')
                                             
    latest_news = XtNews.objects.all().order_by('-date')[0:6]

    return render_to_response('index.html', {"napr_xt_classes": napr_xt_classes,
                                             "geogr_xt_classes": geogr_xt_classes,
                                             "latest_news":latest_news},
                              context_instance=RequestContext(request))


def xtreport_list(request, part):
    return render_to_response('repo_list.html', {},
                              context_instance=RequestContext(request))


def xtreport_item(request, part, slug):
    return render_to_response('repo.html', {},
                              context_instance=RequestContext(request))


def xtclass(request, slug):
    xtcdescription_xtclass = XtClass.objects.get(vcode=slug)
    return render_to_response('class.html', {"xtcdescription_xtclass": xtcdescription_xtclass},
                              context_instance=RequestContext(request))
