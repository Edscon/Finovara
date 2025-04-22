from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet

class ApiKey(models.Model):
    name = models.CharField(max_length=255, default="default")
    key = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key 
