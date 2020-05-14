# Generated by Django 3.0.4 on 2020-04-30 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageng',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageng_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('imageng_nav', models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Изображение главная',
                'verbose_name_plural': 'Изображение главная',
            },
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_title', models.CharField(max_length=200, verbose_name='Название новости')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('new_text', models.TextField(verbose_name='Текст новости')),
                ('created_date', models.DateTimeField(verbose_name='дата размещения')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]
