from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class Place(models.Model):
    """Model representing place of interest"""
    title = models.CharField(max_length=200,
                             help_text="Название точки",
                             )
    description_short = models.TextField("Короткое описание ",
                                         blank=True,
                                         default='',
                                         help_text="Короткое описание точки",
                                         )
    description_long = HTMLField("Полное описание",
                                 blank=True,
                                 default='',
                                 help_text="Полное описание точки",
                                 )
    lat = models.DecimalField('Широта', max_digits=9, decimal_places=6)
    long = models.DecimalField('Долгота', max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title


class Image(models.Model):
    """Model representing places images"""
    title = models.CharField('Имя картинки',
                             max_length=200,
                             blank=True,
                             help_text="Название картинки",
                             default='',
                             )

    place = models.ForeignKey(Place,
                              verbose_name='Место',
                              related_name='images',
                              on_delete=models.CASCADE,
                              help_text='К какому месту отнести картинку'
                              )

    sorting_priority = models.PositiveSmallIntegerField('Сортировка',
                                                        default=0,
                                                        blank=True,
                                                        help_text='приоритет сортировки, по умолчанию 1',
                                                        )

    image = models.ImageField(help_text='Изображение для модели')

    class Meta:
        ordering = ['sorting_priority']

    def __str__(self):
        return f'{self.sorting_priority} {self.place.title}'
