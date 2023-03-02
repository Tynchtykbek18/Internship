import uuid
from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.
class Users(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    surname = models.TextField()
    email = models.TextField(unique=True)
    password = models.TextField(max_length=14)
    address = models.TextField()
    phone_number = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'