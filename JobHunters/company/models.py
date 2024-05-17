from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateField()
    picture = models.ImageField(upload_to='media', default="hekla-logo.png")
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)  # Store logos in media/company_logos/

    def __str__(self):
        return self.name
