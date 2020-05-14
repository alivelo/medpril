from django.shortcuts import render
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View
from .models import corruption_text,corruption_file
def corrupt(request):
    cort = corruption_text.objects.all()
    corf=corruption_file.objects.all()
    return render(request, 'corruption.html',{'cort':cort,'corf':corf})


