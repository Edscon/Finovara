from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username