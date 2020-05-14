from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import managing,staff_file,med
def staf(request):

    staf= staff_file.objects.all()
    medl= med.objects.all()
    return render(request, 'staff.html',{'staf':staf,'medl':medl})

def manager(request):
    manag = managing.objects.all()
    return render(request, 'upr_staff.html',{'manag':manag})
# Create your views here.

