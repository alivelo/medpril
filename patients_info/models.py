from django.conf import settings
from django.db import models
from django.utils import timezone


class informeit(models.Model):
    informeit_title = models.CharField('Название ', max_length=200)
    informeit_text = models.TextField('Текст информации', null=True)
    informeit_file = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.informeit_title

    class Meta:
        verbose_name = 'Информация для поциента'
        verbose_name_plural = 'Информация для поциентов'


class description (models.Model):
    description_title = models.CharField('Название ',max_length=200)
    description_text = models.TextField('Текст информации')
    def __str__(self):
        return self.description_title
    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'

