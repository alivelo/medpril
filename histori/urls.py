from django.conf.urls import  url, include
from django.urls import path
from django.contrib import  admin
from histori import  views
from django.conf.urls.static import static
app_name='historis'
urlpatterns=[
    path('',views.historis,name='historis')]
