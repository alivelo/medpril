from django.conf.urls import  url, include
from django.contrib import  admin
from documents import  views
from django.urls import path
from django.conf.urls.static import static
app_name='documents'
urlpatterns=[
        path('',views.documents,name='documents')]