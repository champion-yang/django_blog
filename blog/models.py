from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name='blog_posts', null=True, on_delete=models.SET_NULL)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title
