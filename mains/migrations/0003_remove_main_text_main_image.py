# Generated by Django 3.0.4 on 2020-05-08 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0002_auto_20200508_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_text',
            name='main_image',
        ),
    ]
