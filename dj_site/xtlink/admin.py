from dj_site.xtlink.models import XtLink
from django.contrib import admin


class XtLinkAdmin(admin.ModelAdmin):
    list_display = ('link', 'link_text', 'link_desc', 'link_author_id', 'link_isdirect', 'link_sort')
    search_fields = ['link', 'link_text']
    fieldsets = (
        (None, {
            'fields': ('link', 'link_text', 'link_desc', 'link_author_id', 'link_isdirect', 'link_sort')
        }),
        )
    

admin.site.register(XtLink, XtLinkAdmin)