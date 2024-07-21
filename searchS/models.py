# models.py
from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    tests = models.CharField(max_length=255)
    address = models.CharField(max_length=255, default='')
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, default='')
    cost = models.DecimalField(max_digits=10, decimal_places=2)  
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=255, default='')
    medicine = models.CharField(max_length=255, default='')
    cost = models.CharField(max_length=10, default='')  
    address = models.CharField(max_length=255, default='')
    location = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    map_link = models.URLField(blank=True, null=True)
    side_effects = models.TextField(blank=True)
    uses = models.TextField(blank=True)

    def __str__(self):
        return self.store_name


