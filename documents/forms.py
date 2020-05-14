from django import forms
from .models import document_file

class DocumentForm(forms.ModelForm):
    class Meta:
        model = document_file
        fields = ('document_file_title', 'document_file_files', )