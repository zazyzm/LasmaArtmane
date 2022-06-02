from django.contrib import admin
from .models import Section


class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    list_filter = ('name', 'is_active',)
    list_editable = ('is_active',)
    search_fields = ('name', 'is_active')
    list_per_page = 10


admin.site.register(Section, SectionAdmin)
