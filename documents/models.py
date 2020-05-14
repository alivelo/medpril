from django.conf import settings
from django.db import models
from django.utils import timezone
from django.forms.models import modelform_factory
class document (models.Model):

    document_title = models.CharField('Заголовок', max_length=20)
    document_list = models.TextField('Текст')
    def __str__(self):
        return self.document_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class document_file(models.Model):
    document_file_title = models.CharField('Заголовок', max_length=200)
    document_file_files = models.FileField('файл', upload_to='user_media', null=True)



def __str__(self):
    return self.document_file_title
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'



