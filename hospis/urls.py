from django.conf.urls import  url, include
from django.contrib import  admin
from hospis import  views
from django.urls import path
from django.conf.urls.static import static
app_name='hospis'
urlpatterns=[
    path('',views.hospi,name='hospi'),

]