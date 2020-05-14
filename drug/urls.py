from django.conf.urls import  url, include
from django.urls import path
from django.contrib import  admin
from drug import  views
from django.conf.urls.static import static
app_name='drug'
urlpatterns=[
    path('',views.drugst,name='drugst')]
