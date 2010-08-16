from dj_site.xtobject.models import XtObject, XtObjecttype, XtC2O
from django.contrib import admin


class XtC2OInlineXtObject(admin.TabularInline):
    model = XtC2O
    fk_name = "xtobject"
    extra = 1


class XtObjectAdmin(admin.ModelAdmin):
    list_display = ('status', 'freeedit', 'object_id', 'objurl') #, 'xtobjecttype') I have some strange error here
    list_filter = ('status', 'freeedit', 'xtobjecttype')
    fieldsets = (
        (None, {
            'fields': ('status', 'freeedit', 'xtobjecttype', 'content_type', 'object_id', 'objurl', 'susshabl', 'objfavour', 'view', 'comment'),
        }),
        )
    inlines = [XtC2OInlineXtObject]


class XtObjecttypeAdmin(admin.ModelAdmin):
    list_display = ('otname', 'ot_table_name')
    fieldsets = (
        (None, {
            'fields': ('otname', 'ot_table_name'),
        }),
        )


admin.site.register(XtObject, XtObjectAdmin)
admin.site.register(XtObjecttype, XtObjecttypeAdmin)
