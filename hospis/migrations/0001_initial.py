# Generated by Django 3.0.4 on 2020-04-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospis_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospis_file_title', models.CharField(max_length=200, verbose_name='Заголовок ')),
                ('hospis_file_files', models.FileField(null=True, upload_to='uploads/', verbose_name='файл')),
            ],
            options={
                'verbose_name': 'Дополнительный файл',
                'verbose_name_plural': 'Дополнительные файлы',
            },
        ),
        migrations.CreateModel(
            name='hospis_start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospis_start_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение ')),
                ('hospis_start_name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('hospis_start_text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Инфыормация о отделе',
                'verbose_name_plural': 'Информация о отделе',
            },
        ),
    ]
