from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import  Http404,HttpResponseRedirect
from django.views.generic.base import View
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import document,document_file


def documents(request):

    doc = document_file.objects.all()
    doct=document.objects.all()
    return render(request, 'documents.html',{'doc':doc,'doct':doct})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = DocumentForm()
    return render(request, 'doc.html', {
        'form': form
    })





