from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import drug, drug_file


class drugAdminForm(forms.ModelForm):
    drug_list = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = drug
        fields = '__all__'

class drugAdmin(admin.ModelAdmin):
    list_filter = ['drug_title']
    search_fields = ['drug_title','drug_list']
    form = drugAdminForm
class Meta:

    model = drug
admin.site.register(drug,drugAdmin)

class drug_fileAdmin(admin.ModelAdmin):
    list_filter = ['drug_file_title']
    search_fields = ['drug_file_title']
class Meta:

    model = drug_file
admin.site.register(drug_file,drug_fileAdmin)