from django.contrib import admin
from .models import job, job_file
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class jobAdminForm(forms.ModelForm):
    job_list= forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = job
        fields = '__all__'

class jobAdmin(admin.ModelAdmin):
    list_filter = ['job_title']
    search_fields = ['job_list', 'ob_title']
    form = jobAdminForm

class Meta:
    model = job
admin.site.register(job,jobAdmin)


class job_fileAdmin(admin.ModelAdmin):
    list_filter = ['job_file_title']
    search_fields = ['job_file_title', 'job_file_files']


class Meta:
    model = job_file
admin.site.register(job_file,job_fileAdmin)

