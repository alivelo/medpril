from django.conf import settings
from django.db import models
from django.utils import timezone


class message(models.Model):
    message_text = models.TextField('текст сообщения')
    message_name = models.CharField('Имя отправителя ', max_length=200)
    message_phone = models.CharField('телефон ', max_length=20)
    massage_email = models.EmailField('mail', max_length=50)


    def __str__(self):
     return self.massage_name

    class Meta:
        verbose_name = 'Сообщения пользователя'
        verbose_name_plural = 'Сообщение пользователей'


class units (models.Model):
    units_name = models.TextField('Подразделение')
    units_adres = models.TextField('адрес')
    units_phone = models.CharField('Телефон', max_length=20)
    units_index = models.CharField('Индекс', max_length=6)

    def __str__(self):
        return self.units_name
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class dop_info (models.Model):
    dop_info_title = models.CharField('Название ', max_length=200)
    dop_info_text = models.TextField('текст')
    dop_info_image = models.FileField('Фото', null=True, blank=True)
    dop_info_files = models.FileField('файл', upload_to='uploads/', null=True,blank=True)

    def __str__(self):
        return self.dop_info_title

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'

class Comment (models.Model):
    email = models.EmailField('Email ')
    name = models.CharField('Имя',max_length=100)
    message = models.TextField('Сообщение', max_length=5000)
    phone=models.CharField('Телефон',max_length=30)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Контактная форма '
        verbose_name_plural = 'Контактная форма'

