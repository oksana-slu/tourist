from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
    napr_xt_classes = [] #XtClass.objects.filter(nclasstype=1)[:11]
    return render_to_response('index.html', {"napr_xt_classes": napr_xt_classes}, 
                              context_instance=RequestContext(request))
                              
                              
def xtreport_list(request, part):
    return render_to_response('repo_list.html', {}, 
                              context_instance=RequestContext(request))
                              
                              
                              
def xtreport_item(request, part, slug):
    return render_to_response('repo.html', {}, 
                              context_instance=RequestContext(request))
                              
                              
def xtclass(request, slug):
    return render_to_response('class.html', {}, 
                              context_instance=RequestContext(request))