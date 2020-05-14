from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime


class news(models.Model):
    new_title = models.CharField('Название новости', max_length=200)
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



class imageng (models.Model):
    imageng_title = models.CharField('Заголовок', max_length=200)
    imageng_nav = models.FileField('Изображение', upload_to='media/',null=True, blank=True)

    def __str__(self):
        return self.imageng_title

    class Meta:
        verbose_name = 'Изображение главная'
        verbose_name_plural = 'Изображение главная'

class main_text (models.Model):
    main_name = models.CharField('Заголовок', max_length=200, null=True, blank=True, default=None)
    main_text = models.TextField('Описание')
    def __str__(self):
        return self.main_name

    class Meta:
        verbose_name = 'Дополнительная информация'
        verbose_name_plural = 'Дополнительная информация'

        class managing(models.Model):
            managing_image = models.FileField('Фото', null=True, blank=True)
            managing_fio = models.CharField('Фамилия', max_length=30)
            managing_name = models.CharField('Имя', max_length=20)
            managing_middle = models.CharField('Отчество', max_length=40, null=True)
            managing_position = models.TextField('Должность')
            managing_phone = models.TextField('Телефон')

            def __str__(self):
                return self.managing_name

            class Meta:
                verbose_name = 'Управляющий персонал'
                verbose_name_plural = 'Управляющий персонал'

        class staff_file(models.Model):
            staf_file_title = models.CharField('Название ', max_length=200)
            staff_file_files = models.FileField('файл', upload_to='uploads/', null=True)

            def __str__(self):
                return self.staf_file_title

            class Meta:
                verbose_name = 'Мед работники файл'
                verbose_name_plural = 'Мед работники файлы'


