from django.conf.urls import  url, include
from django.contrib import  admin
from corruption import  views
from django.urls import path
from django.conf.urls.static import static
app_name='corrupt'
urlpatterns=[
        path('',views.corrupt,name='corrupt')]