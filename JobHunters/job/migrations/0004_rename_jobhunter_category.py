# Generated by Django 5.0.6 on 2024-05-15 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_job_full_part_time_job_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='JobHunter',
            new_name='Category',
        ),
    ]