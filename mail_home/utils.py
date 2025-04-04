from django.core.mail import EmailMultiAlternatives, get_connection, EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def send_mail_func(subject, template_path, context, from_user, recipient_list, text_content=None, attachments=None, signature=None):
    try:
        if from_user not in settings.EMAIL_USERS:
            raise ValueError(f"Email user '{from_user}' not configured")
        
        user_config = settings.EMAIL_USERS[from_user]

        connection = get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=user_config['email'],
            password=user_config['password'],
            use_tls=settings.EMAIL_USE_TLS,
        )

        # Render the HTML template with context
        html_content = render_to_string(template_path, context)

        if signature:
            html_content += f"<br><br>{signature}"
            if text_content:
                text_content += f"\n\n{signature}"
        
        # Set up the email
        # msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        # msg.attach_alternative(html_content, "text/html")
        # msg.send()

        email = EmailMultiAlternatives(
            subject=subject,
            body=html_content,
            from_email=user_config['email'],
            to=recipient_list,
            connection=connection,
        )

        email.attach_alternative(html_content, "text/html")
        
        if attachments:
            for attachment in attachments:
                attachment.seek(0)
                file_content = attachment.read()

                email.attach(
                    filename=attachment.name, 
                    content=file_content, 
                    mimetype=attachment.content_type
                )

        email.send()
        
        return True
    except Exception as e:
        print(str(e))
        return False
