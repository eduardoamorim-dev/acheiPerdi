# lostitems/admin.py

from django.contrib import admin
from .models import LostItem

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'lost_location', 'contact_info', 'created_at')
    list_filter = ('created_at', 'lost_location')
    search_fields = ('name', 'description', 'lost_location', 'contact_info')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('Informações do Item', {
            'fields': ('name', 'description', 'image', 'lost_location')
        }),
        ('Contato', {
            'fields': ('contact_info', 'additional_comments')
        }),
        ('Metadados', {
            'fields': ('created_at',)
        }),
    )