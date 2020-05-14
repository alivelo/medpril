from django.contrib import admin
from .models import document, document_file
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class doctAdminForm(forms.ModelForm):
    document_list= forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = document
        fields = '__all__'


class documentAdmin (admin.ModelAdmin):

    list_filter=['document_title','document_list']
    search_fields=['document_list','document_title']
    form = doctAdminForm

class Meta:
    model = document
    admin.site.register(document, documentAdmin)


class document_fileAdmin(admin.ModelAdmin):
    list_filter = ['document_file_title']
    search_fields = ['document_file_title', 'document_file_files']


class Meta:
    model = document_file
    admin.site.register(document_file, document_fileAdmin)