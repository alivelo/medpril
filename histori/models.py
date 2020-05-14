from django.conf import settings
from django.db import models
from django.utils import timezone

class Histori  (models.Model):

    histori_name = models.CharField('Заголовок', max_length=200)
    histori_text = models.TextField('Текст')

    def __str__(self):
        return self.histori_name
    class Meta:
        verbose_name = 'История диспансера'
        verbose_name_plural = 'История диспансера'

class coment  (models.Model):
    coment_name=models.CharField('имя автора', max_length=200)
    coment_text = models.TextField('Текст')

    def __str__(self):
        return self.coment_name
    class Meta:
        verbose_name = 'коментарий'
        verbose_name_plural = 'Коментарии'

