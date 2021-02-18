from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    location = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    landline = models.CharField(max_length=20, blank=True)