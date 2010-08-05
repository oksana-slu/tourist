from dj_site.xtclass.models import XtC2C, XtClass, XtClasstype
from django.contrib import admin

class XtClassAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'vname', 'vcode', 'xtcdescription', 'xtclasstype', 'class_order')
    search_fields = ['vname', 'vcode']
    list_filter = ('xtclasstype', 'class_order')
    

    
    
class XtC2CAdmin(admin.ModelAdmin):
    list_display = ('parent', 'child')


admin.site.register(XtC2C, XtC2CAdmin)
admin.site.register(XtClass, XtClassAdmin)
admin.site.register(XtClasstype)