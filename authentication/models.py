from django.contrib.auth.models import AbstractUser
from django.db import models

ROLE_CHOICES = ('admin', 'user')


class User(AbstractUser):
    phone = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=35, null=True)
    address = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)

