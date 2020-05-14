from django.shortcuts import render
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View

from .models import hospis_start,hospis_file
def hospi(request):
    hoss = hospis_start.objects.all()
    hosf=hospis_file.objects.all()
    return render(request, 'hospis.html',{'hoss':hoss,'hosf':hosf})
