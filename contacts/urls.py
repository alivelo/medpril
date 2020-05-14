from django.conf.urls import  url, include
from django.contrib import  admin
from contacts import  views
from django.urls import path
from django.conf.urls.static import static

app_name='contact'
urlpatterns=[
    path('',views.contact,name='contact'),


]