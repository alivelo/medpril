from django.shortcuts import render
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View
from .models import job,job_file
def jobs(request):

    jobs = job.objects.all()
    jobf=job_file.objects.all()
    return render(request, 'job.html',{'jobs':jobs,'jobf':jobf})
# Create your views here.

