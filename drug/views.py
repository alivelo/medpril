from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import drug, drug_file
def drugst(request):

    drugs = drug.objects.all()
    drugf = drug_file.objects.all()
    return render(request, 'drug.html',{'drugs':drugs,'drugf':drugf})
