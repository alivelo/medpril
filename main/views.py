from django.shortcuts import render
from .models import news, imageng
def main(request):
    title_news=news.objects.order_by('-created_date')[:5]
    return render(request, 'contact.html',{'title_news':title_news})
# Create your views here.
