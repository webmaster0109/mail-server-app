from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from io import BytesIO

def send_mail_func(subject, text_content, template_path, context, emails):
    try:
        # Render the HTML template with context
        html_content = render_to_string(template_path, context)
        
        from_email = settings.EMAIL_HOST_USER
        recipient_list = emails # Add recipient emails here
        
        # Set up the email
        msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        
        return True
    except Exception as e:
        return str(e)
