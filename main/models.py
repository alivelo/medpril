from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class news(models.Model):
    new_title = models.CharField('Название новости', max_length=200)
    image = models.FileField('Изображение', upload_to='media/',null=True, blank=True, default=None)
    new_text = models.TextField('Текст новости')
    created_date = models.DateTimeField('дата размещения')

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def was_published_recently(self):
        return self.created_data >= (timezone.now() - datetime.timedelta(days=30))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

class imageng (models.Model):
    imageng_title = models.CharField('Заголовок', max_length=200)
    imageng_nav = models.FileField('Изображение',upload_to='media/', null=True, blank=True, default=None)

    def __str__(self):
        return self.imageng_title

    class Meta:
        verbose_name = 'Изображение главная'
        verbose_name_plural = 'Изображение главная'


class main_text  (models.Model):
    main_name = models.CharField('Заголовок', max_length=200, null=True, blank=True)
    main_image = models.FileField('Фото', null=True, blank=True, default=None)
    main_text = models.TextField('Описание')
    def __str__(self):
        return self.main_name