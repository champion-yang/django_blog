from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import BlogArticles


# 设置相应的表现形式
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author', )
    date_hierarchy = 'publish'
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogArticlesAdmin)