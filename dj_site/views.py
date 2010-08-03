from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', {}, 
                              context_instance=RequestContext(request))
                              
                              
def xtreport_list(request):
    return render_to_response('repo_list.html', {}, 
                              context_instance=RequestContext(request))
                              
                              
                              
def xtreport_item(request, slug):
    return render_to_response('repo.html', {}, 
                              context_instance=RequestContext(request))
                              
                              
def xtclass(request, slug):
    return render_to_response('class.html', {}, 
                              context_instance=RequestContext(request))