# Generated by Django 3.0.4 on 2020-05-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drug', '0002_auto_20200510_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug_file',
            name='drug_file_files',
            field=models.FileField(null=True, upload_to='user_media', verbose_name='файл'),
        ),
    ]