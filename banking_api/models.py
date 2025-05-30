from django.db import models

# Create your models here.

class Institutions(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    bic = models.CharField(max_length=20)
    transaction_total_days = models.PositiveIntegerField()
    max_access_valid_for_days = models.PositiveIntegerField()
    logo = models.URLField()
    countries = models.JSONField()

    def __str__(self):
        return self.name