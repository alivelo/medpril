from django.conf import settings
from django.db import models
from django.utils import timezone
from django.forms.models import modelform_factory
class uporg (models.Model):

    uporg_title = models.CharField('Заголовок', max_length=20)
    uporg_list = models.TextField('Текст')
    def __str__(self):
        return self.uporg_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class up_file(models.Model):
    up_file_title = models.CharField('Заголовок', max_length=200)
    upt_file_files = models.FileField('файл', upload_to='user_media', null=True)



def __str__(self):
    return self.up_file_title
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class unit (models.Model):
    unit_name = models.TextField('Организация')
    unit_adres = models.TextField('адрес')
    unit_phone = models.CharField('Телефон', max_length=20)


    def __str__(self):
        return self.unit_name
    class Meta:
        verbose_name = 'Организации'
        verbose_name_plural = 'Организация'

