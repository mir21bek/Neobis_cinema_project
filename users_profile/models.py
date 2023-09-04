from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .user_manager import UserManager


class UserProfile(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    token_auth = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return self.email




