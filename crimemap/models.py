from django.db import models

# Create your models here.

class Crime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return f"{self.location} on {self.date} at {self.time}"

from django.contrib import admin
admin.site.register(Crime)