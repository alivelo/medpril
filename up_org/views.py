from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import uporg, up_file,unit
def upgrups(request):

    upo = uporg.objects.all()
    up= up_file.objects.all()
    units = unit.objects.all()
    return render(request, 'uporg.html',{'upo':upo,'up':up,'units':units})







