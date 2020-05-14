from django import forms
from django.contrib import admin
from .models import news, Photo,main_text
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class nAdminForm(admin.TabularInline):
    model = news
    extra=0

class iAdminForm(admin.TabularInline):
    model = main_text
    extra=0

class newsAdminForm(forms.ModelForm):
    new_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = news
        fields = '__all__'


class newAdmin(admin.ModelAdmin):
    list_filter = ['new_title', 'created_date']
    search_fields = ['new_title', 'new_text']
    form=newsAdminForm

class Meta:
    model = news


admin.site.register(news, newAdmin)



class mainAdminForm(forms.ModelForm):
    main_text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = main_text
        fields = '__all__'


class mainAdmin(admin.ModelAdmin):
    list_filter = ['main_name']
    search_fields = ['main_text', 'main_name']
    form=mainAdminForm


class Meta:
    model = main_text


admin.site.register(main_text, mainAdmin)



admin.site.site_title ="Панель админестратора"
admin.site.site_header ="Панель админестратора"


@admin.register(Photo)
class PhotoCarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'width', 'height')
    exclude = ('width', 'height')
    list_display_links = ('title', 'timestamp')

    class Meta:
        model = Photo
