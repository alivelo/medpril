from django.conf import settings
from django.db import models
from django.utils import timezone

class managing  (models.Model):
    managing_image = models.FileField('Фото', null=True, blank=True)
    managing_fio = models.CharField('Фамилия', max_length=30)
    managing_name = models.CharField('Имя', max_length=20)
    managing_middle = models.CharField('Отчество', max_length=40, null=True)
    managing_position = models.TextField('Должность')
    managing_phone = models.TextField('Телефон')
    def __str__(self):
        return self.managing_fio + " " + self.managing_name + " " + self.managing_middle

    class Meta:
        verbose_name = 'Управляющий персонал'
        verbose_name_plural = 'Управляющий персонал'


class staff_file(models.Model):
    staf_file_title = models.CharField('Название ', max_length=200)
    staff_file_files = models.FileField('файл', upload_to='user_media', null=True)

    def __str__(self):
        return self.staf_file_title

    class Meta:
        verbose_name = 'Мед работники файл'
        verbose_name_plural = 'Мед работники файлы'

class med  (models.Model):
    med_name = models.CharField('Заголовок', max_length=200)
    med_text = models.TextField('Описание')
    def __str__(self):
        return self.med_name
    class Meta:
        verbose_name = 'Описание мед работкик'
        verbose_name_plural = 'Описание мед работкики'
