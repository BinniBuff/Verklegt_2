from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateField()
    logo = models.ImageField()
    cover_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
