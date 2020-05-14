from django.contrib import admin
from .models import hospis_file, hospis_start
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class hospisAdminForm(forms.ModelForm):
    hospis_start_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = hospis_start
        fields = '__all__'

class hospis_startAdmin(admin.ModelAdmin):
    list_filter = ['hospis_start_name']
    search_fields = ['hospis_start_name','hospis_start_text']
    form = hospisAdminForm
class Meta:

    model = hospis_start
admin.site.register(hospis_start,hospis_startAdmin)

class hospis_fileAdmin(admin.ModelAdmin):
    list_filter = ['hospis_file_title']
    search_fields = ['hospis_file_title']

class Meta:

    model = hospis_file
admin.site.register(hospis_file,hospis_fileAdmin)
