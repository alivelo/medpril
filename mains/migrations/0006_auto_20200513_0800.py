# Generated by Django 3.0.4 on 2020-05-13 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0005_auto_20200513_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
