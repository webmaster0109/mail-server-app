from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_attempt, name="login"),
    path('logout-user/', logout_attempt, name="logout"),
    path('history/', mail_list, name="mail_list"),
    path('mail/<pk>/', mail_template_detail, name="mail_view"),
    path('mail/delete/<int:pk>/', mail_delete, name="mail_delete"),
    path('mail/edit/<int:pk>/', mail_edit_and_resend, name='mail_edit_resend')
]
