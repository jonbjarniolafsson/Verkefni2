from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, default=None, null=True)
    profileimagepath = models.CharField(blank=True, default=None, max_length=50000, null=True)
    workplace = models.CharField(max_length=20, blank=True, default=None, null=True)
    is_active = models.BooleanField()
