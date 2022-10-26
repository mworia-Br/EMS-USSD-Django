from django.db import models

# Create your models here.
class Service(models.Model):
    SERVICECATEGORY_CHOICES = [
        ("RA", "RA"),
        ("FI", "FI"),
        ("RC", "RC"),
        ("ME", "ME"),
        ("SA", "SA"),
        ("DV", "DV"),
        ("SUA", "SUA"),
    ]
    SERVICE_CATEGORY=models.CharField(max_length = 250, choices = SERVICECATEGORY_CHOICES, default = 'Awaiting confirmation')
    service_name=models.CharField(max_length=100)
    start=models.CharField(max_length=250)
    finish=models.CharField(max_length=250)
    #price = models.FloatField()
    identifiers=models.IntegerField() #equivalent to seat number in a bus
    is_available=models.BooleanField(default=True)

    
    def __str__(self) -> str:
        return self.service_name + " " + self.SERVICE_CATEGORY

class Reporting(models.Model):
    STATUS_CHOICES = [ 
    ("Awaiting confirmation", "Awaiting confirmation"),
    ("Dispaching Help", "Dispaching Help"),
    ("Responded", "Responded"),
    ("Cancelled", "Cancelled"),
    ]
    SERVICECATEGORY = models.CharField(max_length = 150)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.CharField(max_length = 150)
    identifier=models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    departure=models.DateTimeField(null=True, blank=True)
    status=models.CharField(max_length = 250, choices = STATUS_CHOICES, default='Awaiting confirmation')


    def __str__(self) -> str:
        return self.SERVICECATEGORY + " " + self.customer + " " + self.status

from django.contrib import admin
admin.site.register(Service)
admin.site.register(Reporting)
