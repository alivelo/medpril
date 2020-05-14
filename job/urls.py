from django.conf.urls import  url, include
from django.urls import path
from django.contrib import  admin
from job import  views
from django.conf.urls.static import static
app_name='job'
urlpatterns=[
    path('',views.jobs,name='job')

]
