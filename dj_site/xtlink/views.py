#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xtobject.models import XtObject
from django import forms


class LinkForm(forms.Form):
    url_name = forms.URLField(label=u'ест')
    showing_text = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea,  max_length=200)


def edit_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            # ...
            return HttpResponseRedirect('/edit_link')
    else:
        form = LinkForm() # An unbound form

    return render_to_response('edit_link.html', {},
                              context_instance=RequestContext(request, {'form': form}))