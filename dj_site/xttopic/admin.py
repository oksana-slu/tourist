#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from dj_site.xttopic.models import XtNews, XtTopic
from django.contrib import admin


class XtNewsAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'description', 'author_id', 'date', 'forum')
    search_fields = ['path', 'title', 'description']
    fieldsets = (
        (None, {
            'fields': ('path', 'title', 'description', 'author_id', 'date', 'forum')
        }),
        )
        
        
class XtTopicAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'description', 'author_id', 'date', 'forum')
    search_fields = ['path', 'title', 'description']
    fieldsets = (
        (None, {
            'fields': ('path', 'title', 'description', 'author_id', 'date', 'forum')
        }),
        )
    

admin.site.register(XtNews, XtNewsAdmin)
admin.site.register(XtTopic, XtTopicAdmin)
