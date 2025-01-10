from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MailHome(models.Model):
    owner = models.ForeignKey(User, related_name='mails', on_delete=models.CASCADE)
    emailUser = models.CharField(max_length=100)
    emails = models.TextField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
    signature = models.TextField(default="", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.emailUser

class Attachment(models.Model):
    mail = models.ForeignKey(MailHome, related_name='attachments', on_delete=models.CASCADE)
    attachments = models.FileField(upload_to='file/attachments/', blank=True, null=True)
    
    def __str__(self):
        return self.attachments.name