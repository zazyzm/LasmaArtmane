from django.contrib import admin
from .models import Picture
from django.utils.html import format_html

class PictureAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img width="100" src="{}" />'.format(obj.picture.url))

    image_tag.short_description = 'Image'
    list_display = ('id', 'name', 'gallery', 'is_active', 'image_tag', 'date')
    list_filter = ('name', 'gallery', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'gallery', 'is_active')
    list_per_page = 10

admin.site.register(Picture, PictureAdmin)
