from django.contrib import admin
from .models import units,message,dop_info

class unitsf (admin.ModelAdmin):
    list_filter=['units_name','units_adres','units_phone','units_index']
    search_fields=['units_name','units_adres','units_phone','units_index']

class Meta:
    model = units
    admin.site.register(units,unitsf)
class dopf (admin.ModelAdmin):
    list_filter =['dop_info_title']
    search_fields =['dop_info_title','dop_info_text','dop_info_image',' dop_info_files']

class Meta:
    model = dop_info

admin.site.register(dop_info,dopf)

class massagef (admin.ModelAdmin):
        list_filter = ['message_name','message_phone','massage_email']
        search_fields = ['message_text','message_name','message_phone','massage_email']

class Meta:
        model = message
admin.site.register(message, massagef)