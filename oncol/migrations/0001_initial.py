# Generated by Django 3.0.4 on 2020-04-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='oncololog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oncololog_name', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('oncololog_image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('oncololog_text', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Кафедра онкологии',
                'verbose_name_plural': 'Кафедра онкологии',
            },
        ),
    ]
