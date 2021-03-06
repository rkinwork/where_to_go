# Generated by Django 3.1.7 on 2021-06-18 10:01

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20210618_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', help_text='Полное описание точки', verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default='', help_text='Короткое описание точки', verbose_name='Короткое описание '),
        ),
    ]
