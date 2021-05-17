from django.shortcuts import render
from .models import BlogArticles
# Create your views here.

import logging
logger = logging.getLogger(__name__)

def blog_title(request):
    blogs = BlogArticles.objects.all()

    return render(request, "blog/title.html", {"blogs": blogs})


def blog_aritcle(request, article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish

    return render(request, "blog/content.html", {"article": article, "publish": pub})