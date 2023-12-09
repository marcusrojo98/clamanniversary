from django.db import models

# Create your models here.
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    description = models.TextField()

class PrayerRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
