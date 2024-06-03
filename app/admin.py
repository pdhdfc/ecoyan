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

from .models import *

admin.site.register(BlogPost)


from django.contrib import admin
from django.utils.html import format_html
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_open')
    list_filter = ('is_open', 'created_at')
    search_fields = ('title', 'description')
    actions = ['make_open', 'make_closed']

    @admin.action(description='Mark selected jobs as open')
    def make_open(self, request, queryset):
        queryset.update(is_open=True)

    @admin.action(description='Mark selected jobs as closed')
    def make_closed(self, request, queryset):
        queryset.update(is_open=False)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'applied_at', 'download_resume')
    list_filter = ('job', 'applied_at')
    search_fields = ('name', 'email', 'job__title')

    def download_resume(self, obj):
        if obj.resume:
            return format_html('<a href="{}" download>Download</a>', obj.resume.url)
        return "No resume uploaded"
    download_resume.short_description = 'Resume'
