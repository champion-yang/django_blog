# coding=utf-8
"""
@auth: xiaobei
@date: 2021/5/8 
@desc:
"""
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 自己写的登陆函数
    # path('', views.user_login, name='user_login'),

    # django 自带的登陆函数
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),

    path('register/', views.register, name='user_register')
]