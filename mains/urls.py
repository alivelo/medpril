from django.conf.urls import  url, include
from django.urls import path
from django.contrib import  admin
from mains import  views
from django.conf.urls.static import static
app_name='mains'
urlpatterns=[
    path('',views.mains,name='mains'),
    path('<int:news_id>/', views.detail, name='detail'),


]

