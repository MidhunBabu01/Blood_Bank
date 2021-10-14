from django.db import models

# Create your models here.
class DonarDetails(models.Model):
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    age = models.IntegerField()
    blood = models.CharField(max_length=7)