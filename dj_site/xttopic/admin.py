from dj_site.xttopic.models import XtNews, XtReport
from django.contrib import admin


class XtNewsAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'description', 'author_id', 'date', 'forum')
    search_fields = ['path', 'title']
    fieldsets = (
        (None, {
            'fields': ('path', 'title', 'description', 'author_id', 'date', 'forum')
        }),
        )
        
        
class XtReportAdmin(admin.ModelAdmin):
    list_display = ('path', 'title', 'description', 'author_id', 'date', 'forum')
    search_fields = ['path', 'title']
    fieldsets = (
        (None, {
            'fields': ('path', 'title', 'description', 'author_id', 'date', 'forum')
        }),
        )
    

admin.site.register(XtNews, XtNewsAdmin)
admin.site.register(XtReport, XtReportAdmin)