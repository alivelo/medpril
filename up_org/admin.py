from django.contrib import admin
from .models import unit,up_file,uporg
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class uporgAdminForm(forms.ModelForm):
    uporg_list= forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = uporg
        fields = '__all__'


class uporgAdmin (admin.ModelAdmin):

    list_filter=['uporg_title','uporg_list']
    search_fields=['uporg_title','uporg_list']
    form = uporgAdminForm

class Meta:
    model = uporg
    admin.site.register(uporg, uporgAdmin)



class up_file_fileAdmin(admin.ModelAdmin):
    list_filter = ['up_file_title']
    search_fields = ['up_file_title']


class Meta:
    model = up_file
    admin.site.register(up_file, up_file_fileAdmin)


class unitAdmin (admin.ModelAdmin):

    list_filter=['unit_name','unit_adres']
    search_fields=['unit_name','unit_adres']


class Meta:
    model = unit
    admin.site.register(unit, unitAdmin)
