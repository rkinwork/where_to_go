# Generated by Django 3.1.7 on 2021-06-18 09:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20210618_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, default='', help_text='Название картинки', max_length=200, verbose_name='Имя картинки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(help_text='Полное описание точки', verbose_name='Полное описание'),
        ),
    ]
