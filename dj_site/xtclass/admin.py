from dj_site.xtclass.models import XtC2C, XtClass, XtClasstype
from dj_site.xtobject.models import XtC2O
from django.contrib import admin


class XtC2OInlineXtClass(admin.TabularInline):
    model = XtC2O
    fk_name = "xtclass"
    extra = 1


class Xtc2cInlineParents(admin.TabularInline):
    model = XtC2C
    fk_name = "child"
    extra = 1


class Xtc2cInlineChilds(admin.TabularInline):
    model = XtC2C
    fk_name = "parent"
    extra = 1

    
class XtClassAdmin(admin.ModelAdmin):
    list_display = ('vname', 'vcode', 'xtcdescription', 'xtclasstype', 'class_order')
    search_fields = ['vname', 'vcode']
    list_filter = ('xtclasstype', 'class_order')
    fieldsets = (
        (None, {
            'fields': ('vname', 'vcode', 'xtcdescription', 'xtclasstype', 'class_order')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('nshablon', 'xtcconst')
        }),
        )
    inlines = [
        Xtc2cInlineParents, Xtc2cInlineChilds, XtC2OInlineXtClass
    ]
      

class XtClasstypeAdmin(admin.ModelAdmin):
    list_display = ('nme', 'xtct_desc')
    fieldsets = (
        (None, {
            'fields': ('nme', 'xtct_desc')
        }),
        )


admin.site.register(XtClass, XtClassAdmin)
admin.site.register(XtClasstype, XtClasstypeAdmin)