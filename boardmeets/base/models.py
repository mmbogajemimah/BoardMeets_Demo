from django.db import models

# Create your models here.
class Organization(models.Model):
    organization_name = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    website = models.CharField(max_length=200)
    stuff_number = models.IntegerField()

    def __str__(self):
        return self.organization_name
    


