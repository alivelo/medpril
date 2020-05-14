from django.conf import settings
from django.db import models
from django.utils import timezone

class job (models.Model):

    job_title = models.CharField('Заголовок', max_length=200)
    job_list = models.TextField('Текст')
    def __str__(self):
        return self.job_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'


class job_file(models.Model):
    job_file_title = models.CharField('Заголовок', max_length=200)
    job_file_files = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.job_file_title

    class Meta:
        verbose_name = 'Вакансии'
        verbose_name_plural = 'Вакансии'
