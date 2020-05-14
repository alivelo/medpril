from django.conf.urls import  url, include
from django.contrib import  admin
from django.urls import path
from patients_info import views
app_name='patients'
urlpatterns=[
    path('',views.patients,name='patients')
]