from django.db import models


# Create your models here.

class Place(models.Model):
    """Model representing place of interest"""
    title = models.CharField(max_length=200,
                             help_text="Название точки")
    description_short = models.TextField("Короткое описание ", help_text="Короткое описание точки")
    description_long = models.TextField("Полное описание", help_text="Полное описание точки")
    lat = models.FloatField('Широта')
    long = models.FloatField('Долгота')

    def __str__(self):
        return self.title
