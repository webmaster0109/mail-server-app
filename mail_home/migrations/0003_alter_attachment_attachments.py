# Generated by Django 5.1.4 on 2025-01-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail_home', '0002_mailhome_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='attachments',
            field=models.FileField(blank=True, null=True, upload_to='file/attachments/'),
        ),
    ]
