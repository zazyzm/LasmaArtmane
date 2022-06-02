from django.contrib import admin
from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'section', 'is_active')
    list_filter = ('name','section', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'section', 'is_active')
    list_per_page = 10


admin.site.register(Gallery, GalleryAdmin)
