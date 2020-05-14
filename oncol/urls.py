from django.conf.urls import  url, include
from django.contrib import  admin
from oncol import views
from django.urls import path
app_name='oncol'
urlpatterns=[
    path('',views.oncolog,name='onlcolog')
]