from django.shortcuts import render, redirect, get_object_or_404   
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json
from .utils import send_mail_func
import re
from django.utils.html import strip_tags
from .models import MailHome, Attachment

def login_attempt(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
        
        user_obj = authenticate(request, username=username, password=password)

        if user_obj:
            login(request, user_obj)
            return JsonResponse({'status': 'success', 'message': 'login successfully'}, status=200)
        
        return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)
    
    if request.user.is_authenticated:
        return redirect('home')
    
    return render(request, template_name="login.html")

def logout_attempt(request):
    if not request.user.is_authenticated:
        # domain_link = request.build_absolute_uri('/')
        return JsonResponse({
            'status': 'error', 
            'message': 'User is not logged in. Signin dashboard!',
            'meta-title': 'Amara hall of Fame Awards - Email Services',
            'meta-descriptions': 'The Amara Hall of Fame Awards is a prestigious annual celebration dedicated to honoring the achievements and contributions of Indian-origin individuals across the globe. From cinematic icons to business pioneers, from musical talents to philanthropic leaders, we recognize the diverse and exceptional impact of Overseas Indians in fields such as cinema, music, business, technology, sports, fashion, medicine, and philanthropy.',
            'meta-image': 'https://ik.imagekit.io/5lj5xs7ii/Logo/amara-logo.png',
            'redirect_link': '/account/login/'}, 
        status=400)
    if request.method != "POST":
        return JsonResponse({'status': 'error', 'message': 'Invalid method requested'}, status=401)
    logout(request)
    return JsonResponse({'status': 'success', 'message': 'logging out...'}, status=200)
    

@login_required(login_url='/account/login/')
def homepage(request):
    if request.method == "POST":
        try:
            # data = json.loads(request.POST.get('data', {}))
            emailUser = request.POST.get('emailUser')
            emails = request.POST.get('emails')
            subject = request.POST.get('subject')
            isSignature = request.POST.get('isSignature')
            content = request.POST.get('textareaData')
            attachments = request.FILES.getlist('file')
            
            plain_text_content = re.sub(r'</p>\s*', '\n', content)  
            plain_text_content = strip_tags(plain_text_content).strip()

            email_list = [email.strip() for email in emails.split(',') if email.strip()]
            text_content = plain_text_content
            template_path = "mail_template.html"

            signature = ""

            if isSignature == "isSignatureActive":
                signature += "<p>Thanks,</p><p>Kamal Dandona</p><p><b>Chairman</b></p><p style='font-style: italic;'>Amara Hall of Fame Awards</p>"

            context = {
                'content': content,
                'signature': signature,
                'isSignature': isSignature
            }

            mail_instance = MailHome.objects.create(
                owner=request.user,
                emailUser=emailUser,
                emails=email_list,
                subject=subject,
                content=content,
                signature=signature
            )

            for attachment in attachments:
                Attachment.objects.create(mail=mail_instance, attachments=attachment)

            send_mail_func(subject, template_path, context, emailUser, email_list, text_content, attachments)

            return JsonResponse({'status': 'success', 'message': 'Send mail successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON payload'}, status=401)
        
    return render(request, template_name="index.html")

@login_required(login_url='/account/login/')
def mail_list(request):
    mails = MailHome.objects.filter(owner=request.user)
    return render(request, template_name="mail_list.html", context={'mails': mails})

@login_required(login_url='/account/login/')
def mail_template_detail(request, pk):
    mail = MailHome.objects.get(owner=request.user, pk=pk)
    content = mail.content
    return render(request, template_name="mail_template.html", context={'mail': mail, 'content': content, 'signature': mail.signature})

@login_required(login_url='/account/login/')
def mail_delete(request, pk):
    if request.method != "POST":
        return JsonResponse({'status': 'error', 'message': 'Invalid method requested'}, status=405)
    try:
        mail = get_object_or_404(MailHome, owner=request.user, pk=pk)
        mail.delete()
        return JsonResponse({'status': 'success', 'message': 'Mail deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    