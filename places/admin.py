from django.contrib import admin

from .models import Place, Image


# Register your models here.
@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
