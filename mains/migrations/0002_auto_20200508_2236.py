# Generated by Django 3.0.4 on 2020-05-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mains', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='main_text',
            options={'verbose_name': 'Дополнительная информация', 'verbose_name_plural': 'Дополнительная информация'},
        ),
        migrations.AlterField(
            model_name='main_text',
            name='main_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Заголовок'),
        ),
    ]
