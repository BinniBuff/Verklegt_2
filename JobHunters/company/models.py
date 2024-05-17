from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    year_of_start = models.DateField()
    logo = models.ImageField(upload_to='logos/')
    cover_image = models.ImageField(null=True, blank=True, upload_to='cover_images/')

    def __str__(self):
        return self.name
