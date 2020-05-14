from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import healthy_file,grupp_healthy,heal



class healAdminForm(forms.ModelForm):
    Heal_list = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = heal
        fields = '__all__'

class healAdmin(admin.ModelAdmin):
    list_filter = ['Heal_title']
    search_fields = ['Heal_title','Heal_list']
    form = healAdminForm
class Meta:

    model = heal
admin.site.register(heal,healAdmin)

class heAdminForm(admin.TabularInline):
    model = healthy_file
    extra=0
class grupp_healthyAdmin(admin.ModelAdmin):
    list_filter = ['grupp_healthy_name']
    search_fields = ['grupp_healthy_name']
    inlines = [heAdminForm]
class Meta:
    model = grupp_healthy
admin.site.register(grupp_healthy,grupp_healthyAdmin)

class healthy_fileAdmin(admin.ModelAdmin):
    list_filter = ['healthy_file_key','hospis_file_title']
    search_fields = ['healthy_file_key','hospis_file_title']

class Meta:

    model = healthy_file
admin.site.register(healthy_file,healthy_fileAdmin)

