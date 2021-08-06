from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Image, Location
from django.utils.html import format_html


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    fk_name = 'location'
    model = Image
    fields = ('image', ('get_image', 'order'))
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return format_html('<img src={} height="200"', obj.image.url)

    get_image.short_description = 'Превью изображения'


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description_short',
        )
    list_display_links = ('title',)
    search_fields = ('title',)
    inlines = (ImageInline,)


class ImageAdmin(admin.ModelAdmin):
    autocomplete_fields = ('location',)


admin.site.register(Location, LocationAdmin)
admin.site.register(Image, ImageAdmin)
