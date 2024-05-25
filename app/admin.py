from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'timestamp']
    search_fields = ['name', 'email', 'phone', 'timestamp']
    list_filter = ['timestamp']

from django.contrib import admin
from .models import BookTestRode

class BookTestRodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'state', 'city', 'timestamp')
    search_fields = ('name', 'email', 'phone', 'state', 'city')
    list_filter = ('state', 'timestamp')
    ordering = ('-timestamp',)

admin.site.register(BookTestRode, BookTestRodeAdmin)
