# Generated by Django 3.1.7 on 2021-05-20 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210430_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='sorting_priority',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='приоритет сортировки, по умолчанию 1', verbose_name='Сортировка'),
        ),
    ]