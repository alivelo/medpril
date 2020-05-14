from django.conf.urls import  url, include
from django.contrib import  admin
from main import  views
from django.urls import path
from django.conf.urls.static import static

urlpatterns=[
    path('',views.main,name='main')
]