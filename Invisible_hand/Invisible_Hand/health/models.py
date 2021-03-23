from django.db import models

# Create your models here.
class HealthCheck(models.Model):
    date = models.DateField()
    leukocyte = models.CharField(max_length=20)
    platelet = models.CharField(max_length=20)
    neutrophil = models.CharField(max_length=20)
    CA199 = models.CharField(max_length=20)
    CA125 = models.CharField(max_length=20)
    CEA = models.CharField(max_length=20)
