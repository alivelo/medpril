from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class news(models.Model):
    new_title = models.CharField('Название новости', max_length=200)
    new_text = models.TextField('Текст новости')
    created_date = models.DateTimeField('дата размещения')

    def __str__(self):
        return self.new_title

    def publish(self):
        self.created_date = timezone.now()
        self.save()


    def was_published_recently(self):
        return self.created_data >= (timezone.now() - datetime.timedelta(days=30))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'



class Photo(models.Model):
    title = models.CharField(max_length=60, default='', blank=True)
    description = models.TextField(max_length=200, default='', blank=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    image = models.ImageField(width_field="width", height_field="height")
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["timestamp"]
        verbose_name = 'Photo'

class main_text (models.Model):
    main_name = models.CharField('Заголовок', max_length=200, null=True, blank=True, default=None)
    main_text = models.TextField('Описание')
    def __str__(self):
        return self.main_name

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'