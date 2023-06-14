from django.db import models
import uuid

# Create your models here.
class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default=None)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    stuff_number = models.IntegerField()
    address = models.CharField(max_length=255, default=None)
    industry = models.CharField(max_length=255, default=None)
    is_nonprofit = models.BooleanField(default=False)
    established_date = models.DateField(default=None)
    social_media_facebook = models.URLField(null=True, blank=True)
    social_media_twitter = models.URLField(null=True, blank=True)
    social_media_instagram = models.URLField(null=True, blank=True)
    social_media_linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.organization_name
    
class Leader(models.Model):
    id = models.AutoField(primary_key=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    contact = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name


