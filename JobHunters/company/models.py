from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateField()
    logo = models.CharField(max_length=9999)