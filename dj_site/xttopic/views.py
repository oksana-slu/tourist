#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from datetime import datetime
import time
from django.conf import settings
import os
from lxml import etree
import lxml.etree

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from dj_site.xtclass.models import XtClass
from dj_site.xttopic.models import XtNews, XtTopic
from dj_site.xtobject.models import XtObject, XtObjecttype, XtC2O
from django.contrib.contenttypes.models import ContentType
from django import forms
from PIL import Image



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


def add_topic(request, part):
    if request.method == 'POST': 
        form = NewsForm(request.POST) 
        if form.is_valid():
            cleaned_data = form.cleaned_data
            topic_object = XtTopic(title=cleaned_data['name'],
                                 description=cleaned_data['description'],
                                 author_id=request.user.id)
            topic_object.save()

            now_date = datetime.now()
            now_timestamp = time.mktime(now_date.timetuple())
            topic_object.date = int(now_timestamp)

            if part == 'add_report':
               topic_object.path = 'report/%d/' % topic_object.id
               topic_object.save()
               edit_topic = 'edit_report'
               object_object = XtObject(content_object=topic_object,
                                     xtobjecttype_id=2)
               object_object.save()
            else:
               topic_object.path = 'article/%d/' % topic_object.id
               topic_object.save()
               edit_topic = 'edit_article'
               object_object = XtObject(content_object=topic_object,
                                     xtobjecttype_id=1)
               object_object.save()
               
            
            path_name = os.path.join(settings.MEDIA_ROOT, topic_object.path)
            os.mkdir(path_name, 0777)            
            


            return HttpResponseRedirect('/%s/%d' % (str(edit_topic), topic_object.id))
    else:
        form = NewsForm() 

    return render_to_response('add_news.html', {'part': part},
                              context_instance=RequestContext(request, {'form': form}))
                              
                              
class EditNewsForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '70'}),
                              label=u'Название',
                              help_text='Краткое название отображается в заголовке страницы')    
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '3'}),
                                  max_length=200, label=u'Краткое описание',
                                  help_text=' Отображается в списке рядом с иконкой')
    newstext = forms.CharField(widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}),
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
            text.text = cleaned_data['newstext']
            tree = etree.ElementTree(root_tree)
            tree.write(fp, encoding="utf-8", pretty_print=True)
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
                       newstext=news_object.get_text())
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

                            
def edit_topic(request, part, topic_id=None):
    geogr_xt_classes = XtClass.objects.filter(xtclasstype__pk=2,
                                             childs__parent=0).\
                                             order_by('-class_order')
    napr_xt_classes = XtClass.objects.filter(xtclasstype__pk=1,
                                             childs__parent=0).\
                                             order_by('-class_order')
    hrdly_xt_classes = XtClass.objects.filter(xtclasstype__pk=3,
                                             childs__parent=0).\
                                             order_by('-class_order')
    if topic_id is not None:
        topic_object = XtTopic.objects.get(pk=topic_id)
        object_object = XtObject.objects.get(object_id=topic_object.pk,
                                             content_type=ContentType.objects.get_for_model(XtTopic))
                                            
                                            
    if request.method == 'POST':
        checked_xt_classes = [int(item) for item in request.POST.getlist('xtclasschk')]
        form = EditNewsForm(request.POST)
        if 'topicstat' in request.POST:
            topicstat = int(request.POST['topicstat'])
        else:
            topicstat = 3
        if form.is_valid():
            cleaned_data = form.cleaned_data
            topic_object.title = cleaned_data['name']
            topic_object.description = cleaned_data['description']
            topic_object.save()
            
                        
            now_date = datetime.now()
            now_timestamp = time.mktime(now_date.timetuple())
            topic_object.date = int(now_timestamp)
            topic_object.save()
            
            file_name = os.path.join(settings.MEDIA_ROOT, topic_object.path, 'topic.xml')
            fp = open(file_name, "w")
            root_tree = etree.Element("topic")
            sheet = etree.SubElement(root_tree, "sheet")
            text = etree.SubElement(sheet, "text")
            text.text = cleaned_data['newstext']
            tree = etree.ElementTree(root_tree)
            tree.write(fp, encoding="utf-8", pretty_print=True)
            fp.close            
                        
            object_object.status = topicstat
            object_object.save()
                        
            XtC2O.objects.filter(xtobject=object_object).delete()
            for xt_class_item in checked_xt_classes:
                XtC2O.objects.create(xtobject=object_object,
                                     xtclass_id=xt_class_item)
            
            if 'deletelink' in request.POST:                    
                topic_object.delete()
                object_object.delete()
                if part == 'edit_report':
                   add_topic = 'add_report'
                else:
                   add_topic = 'add_article'
                return HttpResponseRedirect('/%s' % add_topic)
            
            return HttpResponseRedirect('/%s/%d' % (str(part), topic_object.id))
    else:
        initial = dict(name=topic_object.title,
                       description=topic_object.description,
                       newstext=topic_object.get_text())
        checked_xt_classes = object_object.xtclass().values_list('xtclass__pk', flat=True)
        topicstat = object_object.status
        
        form = EditNewsForm(initial=initial) 
    return render_to_response('edit_news.html', {"napr_xt_classes": napr_xt_classes,
                                                 "geogr_xt_classes": geogr_xt_classes,
                                                 "hrdly_xt_classes": hrdly_xt_classes,
                                                 "checked_xt_classes": checked_xt_classes,
                                                 "news_id": topic_id,
                                                 "part": part,
                                                 "topicstat": topicstat},
                              context_instance=RequestContext(request, {'form': form}))
                            


class IcoForm(forms.Form):
    ico = forms.ImageField(label=u'Выбор иконки', 
                           help_text='Загружайте только файлы jpg размером не больше 2МБ!')
    
    
def handle_uploaded_file(f, part, news_id):
    if part == 'edit_news':
       part = 'news'
    if part == 'edit_report':
       part = 'report'
    if part == 'edit_article':
       part = 'article'
    file_name = os.path.join(settings.MEDIA_ROOT, part, str(news_id), 'ico.jpg')
    destination = open(file_name, 'wb+')
    destination.write(f.read())
    destination.close()
    
    
def get_file_ico(part, news_id):
    if part == 'edit_news':
       part = 'news'
    if part == 'edit_report':
       part = 'report'
    if part == 'edit_article':
       part = 'article'
    ico_url = os.path.join(settings.MEDIA_URL, part, news_id, 'ico.jpg')
    ico_path = os.path.join(settings.MEDIA_ROOT, part, news_id, 'ico.jpg')
    return ico_url, ico_path


def upload_ico(request, part, news_id):
    if news_id is not None:
       if part != 'edit_news':
          topic_object = XtTopic.objects.get(pk=news_id)
          object_object = XtObject.objects.get(object_id=topic_object.pk,
                                             content_type=ContentType.objects.get_for_model(XtTopic))
       else:
          news_object = XtNews.objects.get(pk=news_id)
          object_object = XtObject.objects.get(object_id=news_object.pk,
                                             content_type=ContentType.objects.get_for_model(XtNews))
    else:
        raise Http404

    ico_url, ico_path = get_file_ico(part, news_id)
    if os.path.isfile(ico_path):
        ico = ico_url
    else:
        ico = None

    if request.method == 'POST':
        form = IcoForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['ico'], part, news_id)
            return HttpResponseRedirect('/upload_ico/%s/%s' % (str(part), str(news_id)))
    else:
        form = IcoForm()
    return render_to_response('upload_ico.html', 
                              RequestContext(request, {'form': form, "news_id": news_id, 'ico': ico, "part": part}))
                            
                            
