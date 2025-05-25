from django.db import models
from django.contrib.auth.models import User

class ApiToken(models.Model):
    access_token = models.TextField()
    refresh_token = models.TextField()
    access_expires_at = models.DateTimeField()
    refresh_expires_at = models.DateTimeField()

    def __str__(self):
        return self.access_token 
