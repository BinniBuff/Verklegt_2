from django.db import models
from django.contrib.auth.models import User
from job.models import Job

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('denied', 'Denied'),
        ('accepted', 'Accepted'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')

    # Step 1: Contact Information
    name = models.CharField(max_length=255)
    street_name = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)

    # Step 2: Cover Letter
    cover_letter = models.TextField()

    # Step 3: Experiences
    experience = models.JSONField(default=list)

    # Step 4: References
    references = models.JSONField(default=list)

    def __str__(self):
        return f'{self.user.username} - {self.job.title}'
