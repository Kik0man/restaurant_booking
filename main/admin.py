from django.contrib import admin
from .models import SiteContent, ContactMessage


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ['key', 'title', 'image_preview']
    search_fields = ['key', 'title']
    fields = ['key', 'title', 'content', 'image']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="50" height="50" />'
        return "Нет изображения"

    image_preview.allow_tags = True
    image_preview.short_description = "Превью"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']