from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import news, Photo,main_text

def mains(request):
    title_news = news.objects.order_by('-created_date')[:30]
    maint = main_text.objects.all()
    queryset = Photo.objects.all()



    return render(request, 'news.html', {'title_news':title_news,'maint':maint, "photos": queryset})
def detail(request,news_id):
    try:
        post=news.objects.get(id = news_id )
    except:
        raise Http404('Статья не найдена')
    return render(request, 'new.html',{'post':post})












