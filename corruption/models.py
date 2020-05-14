from django.conf import settings
from django.db import models
from django.utils import timezone

class corruption_text (models.Model):

    corruption_text_title = models.CharField('Заголовок', max_length=400)
    corruption_text_list = models.TextField('Текст')
    def __str__(self):
        return self.corruption_text_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class corruption_file(models.Model):
    corruption_file_title = models.CharField('Заголовок', max_length=200)
    corruption_file_files = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.corruption_file_title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
