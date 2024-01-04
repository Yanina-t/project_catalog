from django.contrib.auth.models import AbstractUser
from django.db import models
NULLABLE = {'blank': True, 'null': True}

# Create your models here.
class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')

    avatar = models.ImageField(upload_to='avatars/', **NULLABLE, verbose_name='аватар')
    phone_number = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
