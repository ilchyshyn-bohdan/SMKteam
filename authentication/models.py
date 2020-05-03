from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField

ROLE_CHOICES = ('admin', 'user')


class User(AbstractUser):
    phone = models.CharField(max_length=30, null=True)
    country = CountryField(max_length=35, null=True)
    address = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    events = models.ManyToManyField('models.Event', null=False, blank=True)

