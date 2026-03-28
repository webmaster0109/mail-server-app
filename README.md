# Send Mail Server

A professional, feature-rich Django-based email management and distribution service. This application provides a complete dashboard for sending bulk emails, managing attachments, utilizing rich-text (HTML) templates, and maintaining a complete history of sent and deleted emails.

This project was built to handle specialized email campaigns, such as those for the Amara Hall of Fame Awards, featuring multiple sender identities, custom signatures, and robust soft-delete (trash/restore) functionality.

## Features

- **Rich-Text Email Composition**: Compose emails using a WYSIWYG editor (TinyMCE) with HTML support.
- **Multiple Sender Configurations**: Easily switch between pre-configured sender email addresses (e.g., `info@domain.com`, `user@domain.com`).
- **Bulk Emailing**: Send to multiple recipients simultaneously by providing a comma-separated list of email addresses.
- **Attachments Support**: Upload and attach multiple files to any outgoing email.
- **Dynamic Signatures**: Optional appendable signatures (e.g., Chairman's signature for official communications).
- **Email History & Resending**: View a complete history of sent emails. Edit and easily resend past campaigns with new recipients or updated content.
- **Trash & Restore**: Soft-delete functionality. Move sent emails to the trash, permanently delete them, or restore them back to your history.
- **User Authentication**: Secure login system ensuring only authorized users can access the dashboard and their specific email history.

## Technology Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL (hosted on Neon)
- **Frontend**: HTML, CSS, JavaScript (Django Templates)
- **Server**: Gunicorn, ASGI/WSGI
- **Media/File Handling**: Pillow

## Prerequisites

- Python 3.8+
- PostgreSQL
- Valid SMTP credentials (e.g., Gmail App Passwords or a dedicated SMTP provider)

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables Configuration (Recommended):**
   *Note: For security best practices, you should avoid hardcoding sensitive credentials in `settings.py`.*

   Create a `.env` file in the root directory and add the following:
   ```env
   # Django Settings
   SECRET_KEY=your-secure-secret-key
   DEBUG=True # Set to False in production

   # Database Settings
   DATABASE_URL=postgresql://user:password@hostname:port/dbname

   # Email Configuration
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True

   # Sender Accounts
   FIRST_USER_EMAIL=user1@example.com
   FIRST_USER_PASSWORD=your-app-password
   SECOND_USER_EMAIL=user2@example.com
   SECOND_USER_PASSWORD=your-app-password
   ```
   *(You will need to install `django-environ` or `python-dotenv` and update `settings.py` to read these variables).*

5. **Apply Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser:**
   To access the application, you need an admin account:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Usage Guide

1. **Login**: Navigate to the homepage. You will be redirected to `/account/login/`. Log in with your superuser or authorized user credentials.
2. **Dashboard**: Once logged in, you can compose a new email. Select your sender identity, enter recipient emails (comma-separated), a subject, and your rich-text content.
3. **Attachments & Signatures**: Attach files using the file input. Toggle the signature checkbox to automatically append the pre-configured official signature.
4. **History (`/history/`)**: View all previously sent emails. Click on any email to view its details.
5. **Edit & Resend**: From the history or detail view, you can edit a previously sent email and resend it to new or existing recipients.
6. **Trash (`/trash/`)**: Deleted emails are moved here. You can permanently delete them or restore them to your history.

## Security Warning

The current repository contains hardcoded database credentials (`tmpPostgres`) and SMTP passwords in `send_mail_server/settings.py`. **It is strongly recommended to immediately rotate these credentials and move them to environment variables before deploying to any production environment.**

## License

This project is licensed under the MIT License - see the LICENSE file for details.
