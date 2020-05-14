from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views.generic.base import View
from .models import oncololog
def oncolog(request):
    oncl = oncololog.objects.all()
    return render(request, 'oncol.html',{'oncl':oncl})
# Create your views here.

