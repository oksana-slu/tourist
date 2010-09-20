#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from datetime import datetime
import time
from django.conf import settings
import os
from lxml import etree
import lxml.etree
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic
from dj_site.xtobject.models import XtObject, XtObjecttype, XtC2O
from django.contrib.contenttypes.models import ContentType
from django import forms


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
                              
                              
class NewsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '70'}),
                              label=u'Название',
                              help_text='Краткое название отображается в заголовке страницы')    
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}),
                                  max_length=200, label=u'Краткое описание',
                                  help_text=' Отображается в списке рядом с иконкой')


def add_news(request):
    if request.method == 'POST': 
        form = NewsForm(request.POST) 
        if form.is_valid():
            cleaned_data = form.cleaned_data
            news_object = XtNews(title=cleaned_data['name'],
                                 description=cleaned_data['description'],
                                 author_id=request.user.id)
            news_object.save()

            now_date = datetime.now()
            now_timestamp = time.mktime(now_date.timetuple())
            news_object.date = int(now_timestamp)

            news_object.path = 'news/%d/' % news_object.id
            news_object.save()
            
            path_name = os.path.join(settings.MEDIA_ROOT, news_object.path)
            os.mkdir(path_name, 0777)            
            
            object_object = XtObject(content_object=news_object,                                         
                                     xtobjecttype_id=5)
            object_object.save()

            return HttpResponseRedirect('/edit_news/%d' % news_object.id) 
    else:
        form = NewsForm() 

    return render_to_response('add_news.html', {},
                              context_instance=RequestContext(request, {'form': form}))
                              
                              
class EditNewsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '70'}),
                              label=u'Название',
                              help_text='Краткое название отображается в заголовке страницы')    
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}),
                                  max_length=200, label=u'Краткое описание',
                                  help_text=' Отображается в списке рядом с иконкой')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}),
                                  label=u'Текст', required=False)


def edit_news(request, news_id=None):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')
    hrdly_xt_classes = XtClass.objects.filter(xtclasstype__pk=3,
                                             childs__parent=0).\
                                             order_by('-class_order')
    if news_id is not None:
        news_object = XtNews.objects.get(pk=news_id)
        object_object = XtObject.objects.get(object_id=news_object.pk,
                                             content_type=ContentType.objects.get_for_model(XtNews))
                                            
                                            
    if request.method == 'POST':
        checked_xt_classes = [int(item) for item in request.POST.getlist('xtclasschk')]
        form = EditNewsForm(request.POST)
        if 'topicstat' in request.POST:
            topicstat = int(request.POST['topicstat'])
        else:
            topicstat = 3
        if form.is_valid():
            cleaned_data = form.cleaned_data
            news_object.title = cleaned_data['name']
            news_object.description = cleaned_data['description']
            news_object.save()
            
                        
            now_date = datetime.now()
            now_timestamp = time.mktime(now_date.timetuple())
            news_object.date = int(now_timestamp)
            news_object.save()
            
            file_name = os.path.join(settings.MEDIA_ROOT, news_object.path, 'topic.xml')
            fp = open(file_name, "w")
            root_tree = etree.Element("topic")
            sheet = etree.SubElement(root_tree, "sheet")
            text = etree.SubElement(sheet, "text")
            text.text = cleaned_data['text']
            tree = etree.ElementTree(root_tree)
            tree.write(fp)
            fp.close            
                        
            object_object.status = topicstat
            object_object.save()
                        
            XtC2O.objects.filter(xtobject=object_object).delete()
            for xt_class_item in checked_xt_classes:
                XtC2O.objects.create(xtobject=object_object,
                                     xtclass_id=xt_class_item)
            
            if 'deletelink' in request.POST:                    
                news_object.delete()                    
                object_object.delete()                
                return HttpResponseRedirect('/add_news')
            
            return HttpResponseRedirect('/edit_news/%d' % news_object.id) 
    else:
        initial = dict(name=news_object.title,
                       description=news_object.description,
                       text=news_object.get_text())
        checked_xt_classes = object_object.xtclass().values_list('xtclass__pk', flat=True)
        topicstat = object_object.status
        
        form = EditNewsForm(initial=initial) 
    return render_to_response('edit_news.html', {"napr_xt_classes": napr_xt_classes,
                                                 "geogr_xt_classes": geogr_xt_classes,
                                                 "hrdly_xt_classes": hrdly_xt_classes,
                                                 "checked_xt_classes": checked_xt_classes,
                                                 "news_id": news_id,
                                                 "topicstat": topicstat},
                              context_instance=RequestContext(request, {'form': form}))


