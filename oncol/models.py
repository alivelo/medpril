from django.conf import settings
from django.db import models
from django.utils import timezone

class oncololog  (models.Model):
    oncololog_name = models.CharField('Заголовок', max_length=200)
    oncololog_text = models.TextField('Описание')
    def __str__(self):
        return self.oncololog_name
    class Meta:
        verbose_name = 'Кафедра онкологии'
        verbose_name_plural = 'Кафедра онкологии'


