from django.db import models
from company.models import Company

# Create your models here.
class JobHunter(models.Model):
    name = models.CharField(max_length=255)

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(JobHunter, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_offer = models.DateField()
    date_expired = models.DateField(null=True, blank=True)