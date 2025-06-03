from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(unique=True, verbose_name='Почта')
    created_at = models.DateTimeField(
        'Дата создания', auto_now_add=True,
    )
