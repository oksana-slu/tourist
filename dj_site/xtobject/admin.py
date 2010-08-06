from dj_site.xtobject.models import XtObject, XtObjecttype, XtC2O
from django.contrib import admin


class XtObjectAdmin(admin.ModelAdmin):
    list_display = ('status', 'freeedit', 'xtobjecttype', 'objid', 'objurl')
    list_filter = ('status', 'freeedit', 'xtobjecttype')
    fieldsets = (
        (None, {
            'fields': ('status', 'freeedit', 'xtobjecttype', 'objid', 'objurl', 'susshabl', 'objfavour', 'view', 'comment')
        }),
        )
        
        
class XtObjecttypeAdmin(admin.ModelAdmin):
    list_display = ('otname', 'ot_table_name')
    fieldsets = (
        (None, {
            'fields': ('otname', 'ot_table_name')
        }),
        )
        
class XtC2OAdmin(admin.ModelAdmin):
    list_display = ('xtclass', 'nclassmain', 'xtobject')


admin.site.register(XtObject, XtObjectAdmin)
admin.site.register(XtObjecttype, XtObjecttypeAdmin)
admin.site.register(XtC2O, XtC2OAdmin)