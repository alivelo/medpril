from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import informeit, description
def patients(request):
    des = description.objects.all()
    inf = informeit.objects.all()
    return render(request, 'patients_info.html',{'des':des,'inf':inf})
# Create your views here.

