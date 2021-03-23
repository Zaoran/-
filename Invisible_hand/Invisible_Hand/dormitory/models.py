from django.db import models

# Create your models here.
class duty(models.Model):
    water = models.IntegerField()
    rubbish = models.IntegerField()