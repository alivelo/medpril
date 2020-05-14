from django.contrib import admin
from .models import informeit, description
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class infoAdminForm(forms.ModelForm):
    informeit_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = informeit
        fields = '__all__'



class informeitAdmin(admin.ModelAdmin):
    list_filter = ['informeit_title']
    search_fields = ['informeit_text', 'informeit_title']
    form=infoAdminForm

class Meta:
        model = informeit
        admin.site.register(informeit,informeitAdmin)

class desAdminForm(forms.ModelForm):
    description_text = forms.CharField(widget=CKEditorUploadingWidget())

class Meta:
        model = description
        fields = '__all__'


class descriptionAdmin(admin.ModelAdmin):
    list_filter = ['description_title']
    search_fields = ['description_title', 'description_text']
    form=desAdminForm

class Meta:
        model = description
        admin.site.register(description,descriptionAdmin)


