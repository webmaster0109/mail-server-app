from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', homepage, name="home"),
    path('login/', login_attempt, name="login"),
    path('logout-user/', logout_attempt, name="logout"),
]
