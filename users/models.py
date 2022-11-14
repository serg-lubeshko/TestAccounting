from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


class MyUser(AbstractUser):
    """ Модель Пользователей """

    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return f'{self.username}'

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
