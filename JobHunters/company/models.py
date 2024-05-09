from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateField()
    logo = models.CharField(max_length=9999)
    def __str__(self):
        return self.name

class CompanyImage(models.Model):
    image = models.CharField(max_length=9999)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    def __str__(self):
        return self.image