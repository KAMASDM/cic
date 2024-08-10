from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email_host = models.CharField(max_length=255, null=True)
    email_port = models.IntegerField(null=True)
    email_username = models.CharField(max_length=255,null=True)
    email_password = models.CharField(max_length=255, null=True)
    email_use_tls = models.BooleanField(default=True,null=True)
    from_email = models.EmailField(null=True)