from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import healthy_file, grupp_healthy,heal
def healthys(request):

    healt = healthy_file.objects.all()
    gryp = grupp_healthy.objects.all()
    heals = heal.objects.all()
    return render(request, 'healthy.html',{'healt':healt,'gryp':gryp,'heals':heals})
