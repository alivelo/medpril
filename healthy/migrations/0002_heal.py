# Generated by Django 3.0.4 on 2020-05-10 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='heal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Heal_title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('Heal_list', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Описание',
                'verbose_name_plural': 'Описание',
            },
        ),
    ]
