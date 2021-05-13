from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)  # 声明与User之间的关系是一一对应的, 并设置了级联删除
    birth = models.DateField(blank=True, null=True)  # blank = true 默认可以为空
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)