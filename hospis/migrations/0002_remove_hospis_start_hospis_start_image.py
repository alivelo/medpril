# Generated by Django 3.0.4 on 2020-05-11 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospis_start',
            name='hospis_start_image',
        ),
    ]