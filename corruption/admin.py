from django.contrib import admin
from .models import corruption_text, corruption_file
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class corAdminForm(forms.ModelForm):
    corruption_text_list= forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = corruption_text
        fields = '__all__'

class corruption_textAdmin(admin.ModelAdmin):
    list_filter = ['corruption_text_title']
    search_fields = ['corruption_text_title','corruption_text_list']
    form = corAdminForm
class Meta:

    model =corruption_text
admin.site.register(corruption_text,corruption_textAdmin)

class corruption_fileAdmin(admin.ModelAdmin):
    list_filter = ['corruption_file_title']
    search_fields = ['corruption_file_title']
class Meta:

    model = corruption_file
admin.site.register(corruption_file,corruption_fileAdmin)