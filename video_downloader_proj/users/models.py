from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_email_verification = models.BooleanField(default=False)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)