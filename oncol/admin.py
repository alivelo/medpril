from django.contrib import admin
from .models import oncololog
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class oncoAdminForm(forms.ModelForm):
    oncololog_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = oncololog
        fields = '__all__'


class oncolologAdmin(admin.ModelAdmin):
    list_filter = ['oncololog_name']
    search_fields = ['oncololog_name','oncololog_text']
    form=oncoAdminForm
class Meta:

    model = oncololog
admin.site.register(oncololog,oncolologAdmin)
