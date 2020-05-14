from django.contrib import admin
from .models import managing, staff_file


class managingAdmin(admin.ModelAdmin):
    list_filter = ['managing_fio','managing_name','managing_middle','managing_position','managing_phone']
    search_fields = ['managing_fio','managing_name','managing_middle','managing_position','managing_phone']
class Meta:

    model = managing
admin.site.register(managing,managingAdmin)

class staff_fileAdmin(admin.ModelAdmin):
    list_filter = ['staf_file_title']
    search_fields = ['staf_file_title']
class Meta:

    model = staff_file
admin.site.register(staff_file,staff_fileAdmin)