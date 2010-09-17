#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xtobject.models import XtObject, XtObjecttype, XtC2O
from dj_site.xtlink.models import XtLink
from django import forms
from django.contrib.contenttypes.models import ContentType

class LinkForm(forms.Form):
    url_name = forms.URLField(widget=forms.TextInput(attrs={'size': '70'}),
                              label=u'Адреc',
                              help_text='В полном формате включая протокол: http://yandex.ru')
    showing_text = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '2'}),
                                   max_length=100, label=u'Текст')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}),
                                  max_length=200, label=u'Описание')


def edit_link(request, link_id=None):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')
    hrdly_xt_classes = XtClass.objects.filter(xtclasstype__pk=3,
                                             childs__parent=0).\
                                             order_by('-class_order')
    link_object = None 
    
    if link_id is not None:
        link_object = XtLink.objects.get(pk=link_id)
        object_object = XtObject.objects.get(object_id=link_object.pk,
                                             content_type=ContentType.objects.get_for_model(XtLink))
    
    
    if request.method == 'POST':
        checked_xt_classes = [int(item) for item in request.POST.getlist('xtclasschk')]
        form = LinkForm(request.POST)        
        if 'topicstat' in request.POST:
            topicstat = int(request.POST['topicstat'])
        else:
            topicstat = 3
        if 'deletelink' in request.POST:
            deletelink = 1
        else:
            deletelink = 0
        if form.is_valid():            
            cleaned_data = form.cleaned_data            
            if link_object is not None:
                link_object.link = cleaned_data['url_name']
                link_object.link_text = cleaned_data['showing_text']
                link_object.link_desc = cleaned_data['description']
                link_object.save()
                object_object.status = topicstat
                object_object.save()
                if deletelink == 0:
                    if topicstat == 3:
                        request.user.message_set.create(message="Ваш линк удачно сохранен до следующего редактирования.")
                    else:
                        request.user.message_set.create(message="Ваш линк удачно сохранен и будет опубликован после проверки.")

            else:
                link_object = XtLink(link=cleaned_data['url_name'],
                                     link_text=cleaned_data['showing_text'],
                                     link_desc=cleaned_data['description'],                                         link_author_id=request.user.id)
                link_object.save()

                object_object = XtObject(content_object=link_object,
                                         status=topicstat,
                                         xtobjecttype_id=3)
                object_object.save()
                if deletelink == 0:
                    if topicstat == 3:
                        request.user.message_set.create(message="Ваш линк удачно сохранен до следующего редактирования.")
                    else:
                        request.user.message_set.create(message="Ваш линк удачно сохранен и будет опубликован после проверки.")
                        
            XtC2O.objects.filter(xtobject=object_object).delete()
            for xt_class_item in checked_xt_classes:
                XtC2O.objects.create(xtobject=object_object,
                                     xtclass_id=xt_class_item)
            if deletelink == 1:                    
                link_object.delete()                    
                object_object.delete()
                request.user.message_set.create(message="Ваш линк удален.")
                return HttpResponseRedirect('/edit_link')                
            
            return HttpResponseRedirect('/edit_link/%s' % link_object.pk)
    else:
        checked_xt_classes = []
        topicstat = None
        initial = None
        if link_object is not None:
            initial = dict(url_name=link_object.link,
                           showing_text=link_object.link_text,
                           description=link_object.link_desc)
            checked_xt_classes = object_object.xtclass().values_list('xtclass__pk', flat=True)
            topicstat = object_object.status
        form = LinkForm(initial=initial)

    
    return render_to_response('edit_link.html', {"napr_xt_classes": napr_xt_classes,
                                                 "geogr_xt_classes": geogr_xt_classes,
                                                 "hrdly_xt_classes": hrdly_xt_classes,
                                                 "checked_xt_classes": checked_xt_classes,
                                                 "link_id": link_id,
                                                 "topicstat": topicstat},
                              context_instance=RequestContext(request, {'form': form}))
