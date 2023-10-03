from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    login = models.CharField(max_length=16, unique=True, null=False)
    last_name = models.CharField(max_length=16)
    