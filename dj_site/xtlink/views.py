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
    url_name = forms.URLField(widget=forms.TextInput(attrs={'size': '106'}),
                              label=u'Адреc',
                              help_text='В полном формате включая протокол: http://yandex.ru')
    showing_text = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '2'}),
                                   max_length=100, label=u'Текст')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}),
                                  max_length=200, label=u'Описание')


def edit_link(request):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')
    hrdly_xt_classes = XtClass.objects.filter(xtclasstype__pk=3,
                                             childs__parent=0).\
                                             order_by('-class_order')
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            # ...
            return HttpResponseRedirect('/edit_link')
    else:
        form = LinkForm()

    return render_to_response('edit_link.html', {"napr_xt_classes": napr_xt_classes,
                                                 "geogr_xt_classes": geogr_xt_classes,
                                                 "hrdly_xt_classes": hrdly_xt_classes},
                              context_instance=RequestContext(request, {'form': form}))
