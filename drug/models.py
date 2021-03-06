from django.conf import settings
from django.db import models
from django.utils import timezone

class drug (models.Model):

    drug_title = models.CharField('Заголовок', max_length=200)
    drug_list = models.TextField('Текст')
    def __str__(self):
        return self.drug_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class drug_file(models.Model):
    drug_file_title = models.CharField('Заголовок', max_length=200)
    drug_file_files = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.drug_file_title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
