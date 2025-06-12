from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class MailHomeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class MailHome(models.Model):
    owner = models.ForeignKey(User, related_name='mails', on_delete=models.CASCADE)
    emailUser = models.CharField(max_length=100)
    emails = models.TextField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    signature = models.TextField(default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = MailHomeManager()
    all_objects = models.Manager()
    
    def __str__(self):
        return self.subject
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
    
    def undelete(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save()

class Attachment(models.Model):
    mail = models.ForeignKey(MailHome, related_name='attachments', on_delete=models.CASCADE)
    attachments = models.FileField(upload_to='file/attachments/', blank=True, null=True)
    
    def __str__(self):
        return self.attachments.name