from django.contrib import admin
from .models import coment,Histori
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class histAdminForm(forms.ModelForm):
    histori_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Histori
        fields = '__all__'

class HistoriAdmin(admin.ModelAdmin):
    list_filter = ['histori_name']
    search_fields = ['histori_name', 'histori_text']
    form= histAdminForm

class Meta:
    model = Histori
admin.site.register(Histori,HistoriAdmin)

class comentAdmin(admin.ModelAdmin):
    list_filter = ['coment_name']
    search_fields = ['coment_text', 'coment_name']


class Meta:
    model = coment
admin.site.register(coment,comentAdmin)
