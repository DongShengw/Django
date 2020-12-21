"""为应用程序users定义URL模式"""
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, authenticate

from . import views
app_name = 'users'
LoginView.template_name = 'users/login.html'

urlpatterns = [
    # 登入界面
    path('login/', LoginView.as_view(), name='login'),

    # 注销
    path('logout/', views.logout_view, name='logout'),

    # 注册页面
    path('register/', views.register, name='register'),
]
