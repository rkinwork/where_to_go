from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin

from .models import Place, Image

IMG_PRVW_HTML_TEMPLATE = """<img src="{url}" max-height = 200px width = 200 />"""


# Register your models here.
class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 0
    readonly_fields = (
        'image_preview',
    )
    fields = (
        'image',
        'sorting_priority',
        'image_preview',
    )

    def image_preview(self, image: Image):
        return format_html(IMG_PRVW_HTML_TEMPLATE,
                           url=image.image.url,
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
