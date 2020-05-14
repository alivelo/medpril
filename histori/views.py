from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import Histori,coment

def historis(request):
    commen= coment.objects.order_by('-created_date')[:30]
    hist = Histori.objects.all()

    return render(request, 'histori.html',{'commen':commen,'hist':hist})
# Create your views here.
