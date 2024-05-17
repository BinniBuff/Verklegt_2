from django.db import models
from company.models import Company
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='application_jobs')

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('interviewed', 'Interviewed'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='application_job_applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application_job_applications')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='submitted')
    applied_at = models.DateTimeField(auto_now_add=True)

    # Add the missing fields with default values
    name = models.CharField(max_length=255, default='')
    street_name = models.CharField(max_length=255, default='')
    house_number = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    postal_code = models.CharField(max_length=20, default='')
    cover_letter = models.TextField(blank=True, default='')
    experience = models.TextField(blank=True, default='')
    references = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"
