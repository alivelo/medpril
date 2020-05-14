from django.conf import settings
from django.db import models
from django.utils import timezone

class grupp_healthy (models.Model):

    grupp_healthy_name = models.CharField('Заголовок', max_length=200)


    def __str__(self):
        return self.grupp_healthy_name
    class Meta:
        verbose_name = 'Заголовок группы'
        verbose_name_plural = 'Заголовок группы'


class healthy_file(models.Model):
    healthy_file_key=models.ForeignKey(grupp_healthy,on_delete=models.CASCADE)
    hospis_file_title = models.CharField('Заголовок ', max_length=200)
    hospis_file_files = models.FileField('файл', upload_to='uploads/', null=True)

    def __str__(self):
        return self.hospis_file_title

    class Meta:
        verbose_name = 'Файл группы'
        verbose_name_plural = 'Файлы группы'


class heal(models.Model):
    Heal_title = models.CharField('Заголовок', max_length=200)
    Heal_list = models.TextField('Текст')

    def __str__(self):
        return self. Heal_title

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описание'
