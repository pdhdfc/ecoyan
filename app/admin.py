from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'timestamp']
    search_fields = ['name', 'email', 'phone', 'timestamp']
    list_filter = ['timestamp']
