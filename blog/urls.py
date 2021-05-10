# coding=utf-8
"""
@auth: xiaobei
@date: 2021/5/8 
@desc:
"""
from django.conf.urls import url
from . import views
from django.urls import path
from blog.views import *


urlpatterns = [
    path('title', blog_title, name='blog_title'),
    path('<int:article_id>', blog_aritcle, name='blog_aritcle'),
]