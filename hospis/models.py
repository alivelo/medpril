from django.conf import settings
from django.db import models
from django.utils import timezone

class hospis_start  (models.Model):
    hospis_start_name = models.CharField('Заголовок', max_length=200)
    hospis_start_text = models.TextField('Текст')

    def __str__(self):
        return self.hospis_start_name
    class Meta:
        verbose_name = 'Инфыормация о отделе'
        verbose_name_plural = 'Информация о отделе'


class hospis_file(models.Model):
    hospis_file_title = models.CharField('Заголовок ', max_length=200)
    hospis_file_files = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.hospis_file_title

    class Meta:
        verbose_name = 'Дополнительный файл'
        verbose_name_plural = 'Дополнительные файлы'
