#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import os
from datetime import date
from lxml import etree

from django.db import models
from django.http import Http404
from django.conf import settings


class XtTopicAbstract(models.Model):
    id = models.AutoField(primary_key=True)
    path = models.CharField(blank=True, max_length=264)
    title = models.TextField()
    description = models.TextField()
    author_id = models.IntegerField()
    date = models.IntegerField(default=0)
    forum = models.IntegerField(default=0)

    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        abstract = True

    def __init__(self, *karg, **kwarg):
        super(XtTopicAbstract, self).__init__(*karg, **kwarg)
        self._sheets_count = None
        
    def dateformat(self):
        return date.fromtimestamp(long(self.date))

    def get_file_text(self):
        file_name = os.path.join(settings.MEDIA_ROOT, self.path, 'topic.xml')
        if os.path.isfile(file_name):
            fp = open(file_name, 'r')
            return fp.read()
        else:
            return None
        
    
    def get_sheets_count(self):
        if self._sheets_count is not None:
            return self._sheets_count
        else:
            file_text = self.get_file_text()
            if file_text is not None:
                root_tree = etree.XML(file_text)
                self._sheets_count = len(root_tree.findall('sheet'))
                return self._sheets_count
            else:
                return 0

    def get_text(self, sheet_number=1):
        text = ''
        file_text = self.get_file_text()
        if file_text:
            root_tree = etree.XML(file_text)
            sheets_tree_list = root_tree.findall('sheet')
            self._sheets_count = len(sheets_tree_list)
            if self._sheets_count < sheet_number:                
                raise Http404
            text = sheets_tree_list[sheet_number-1].find('text').text

        if not text:
            text = "Text is empty"
        return text
        
    def get_ico_url(self):
        url_name = '/' + self.path + 'ico.jpg'
        return url_name


class XtNews(XtTopicAbstract):

    class Meta:
        db_table = u'xt_news'


class XtTopic(XtTopicAbstract):

    class Meta:
        db_table = u'xt_topic'
