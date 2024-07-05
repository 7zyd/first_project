"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import os
import django
import sys
from accounts.acounts import accounts_views as accounts_views
from app01 import views
from django.contrib.auth import views as auth_views

sys.setrecursionlimit(100000)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()



urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin site URLs
    path('index/', views.index, name="index"),
    path('user_list/', views.user_list, name="user_list"),
    path('home/', views.home, name='home'),
    path('app01/', include('app01.urls')),
    path('boards/<int:pk>/', views.board_topics, name='board_topics'),  # Board topics with primary key
    path('boards/<int:pk>/new/', views.new_topic, name='new_topic'),  # New topic with primary key
    path('signup/', accounts_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password reset views
    path('reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html',
                                                        email_template_name='password_reset_email.html',
                                                        subject_template_name='password_reset_subject.txt'),
         name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # Password change views (previously missing)
    path('settings/password/', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name='password_change'),
    path('settings/password/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name='password_change_done'),
]
