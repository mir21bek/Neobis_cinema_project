from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from rest_framework_simplejwt.tokens import RefreshToken


class UserProfile(AbstractUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'

    def __str__(self):
        return self.email
