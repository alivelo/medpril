from django.conf.urls import  url, include
from django.contrib import  admin
from up_org import  views
from django.urls import path
from django.conf.urls.static import static
app_name='up'
urlpatterns=[
        path('',views.upgrups,name='up')]