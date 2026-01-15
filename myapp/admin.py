from django.contrib import admin
from .models import Profile, Document, Gallery


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'bio']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']
    search_fields = ['title', 'description']
    list_filter = ['uploaded_at']
    readonly_fields = ['uploaded_at']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'uploaded_at']
    search_fields = ['title', 'caption']
    list_filter = ['is_featured', 'uploaded_at']
    readonly_fields = ['uploaded_at']
    list_editable = ['is_featured']
