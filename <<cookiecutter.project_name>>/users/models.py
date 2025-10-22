from django.db import models

# Create your models here.
# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # 可自定义扩展字段，如：
    department = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # 添加自定义的 related_name 以避免与默认 User 模型的冲突
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',
        related_query_name='customuser',
    )

    def __str__(self):
        return self.username
