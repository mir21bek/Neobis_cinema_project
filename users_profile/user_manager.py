from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Эл. Почта обьязательно должно запольняться')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)

        user.set_password(password)
        user.save()

        return user

    def create_super_user(self, email, username, password):
        user = self.create_user(email, username, password)

        user.is_superuser = True
        user.is_staff = True

        user.save()
