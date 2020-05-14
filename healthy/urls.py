from django.conf.urls import  url, include
from django.urls import path
from django.contrib import  admin
from healthy import  views
from django.conf.urls.static import static
app_name='healthy'
urlpatterns=[
    path('',views.healthys,name='healthys')]
