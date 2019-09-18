from django.db import models

# Create your models here.
class Facility(models.Model):
    name = models.CharField(max_length=200)
    care_type = models.CharField(max_length=100)
    id_num = models.IntegerField(blank=True)
    cacpacity = models.IntegerField(blank=True)
    level = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200)
    town = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    in_business = models.BooleanField(blank=True, null=True)
    capacity = models.IntegerField(blank=True)
    accs = models.BooleanField(blank=True, null=True)
    erc = models.BooleanField(blank=True, null=True)
