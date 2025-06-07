from django.contrib import admin
from .models import MailHome, Attachment



@admin.register(Attachment)
class AttachmentInline(admin.ModelAdmin):
    model = Attachment
    extra = 1

@admin.register(MailHome)
class MailHomeAdmin(admin.ModelAdmin):
    list_display = ('emailUser', 'subject', 'created_at')
    search_fields = ('emailUser', 'subject')
    inlines = [AttachmentInline]