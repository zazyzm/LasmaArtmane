from django.contrib import admin
from .models import Picture


class PictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gallery', 'is_active')
    list_filter = ('name', 'gallery', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'gallery', 'is_active')
    list_per_page = 10


admin.site.register(Picture, PictureAdmin)
