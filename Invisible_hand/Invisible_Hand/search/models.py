from django.db import models

# Create your models here.
class NameNumber(models.Model):
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    exchange = models.CharField(max_length=20)