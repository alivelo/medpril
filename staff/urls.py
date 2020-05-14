from django.conf.urls import  url, include
from django.contrib import  admin
from django.urls import path
from staff import views
app_name='staff'
urlpatterns=[
    path('staff/',views.staf,name='staff'),
    path('',views.manager,name='manager')
]