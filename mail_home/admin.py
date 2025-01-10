from django.contrib import admin
from .models import MailHome, Attachment



@admin.register(Attachment)
class AttachmentInline(admin.ModelAdmin):
    model = Attachment
    extra = 1

admin.site.register(MailHome)