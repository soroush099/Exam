from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, default="none bio")
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = "profile"
        verbose_name_plural = "profiles"

    def __str__(self):
        return self.username

