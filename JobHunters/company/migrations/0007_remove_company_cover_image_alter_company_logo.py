# Generated by Django 5.0.4 on 2024-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='cover_image',
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logos/'),
        ),
    ]
