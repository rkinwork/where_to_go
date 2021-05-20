from django.contrib import admin

from .models import Place, Image


# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    fields = (
        'image',
        'sorting_priority',
    )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
