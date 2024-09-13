from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from users.managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(
        unique=True,
        db_index=True  # добавляет индекс для данной таблицы, чтобы делать поиск по имейлу быстрее
    )
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=25)

    objects = CustomUserManager()

    # Переопределяем groups с уникальным related_name
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )

    # Переопределяем user_permissions с уникальным related_name
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'