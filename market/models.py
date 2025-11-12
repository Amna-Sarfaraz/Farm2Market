from django.db import models

class Farmer(models.Model):
    name = models.CharField(max_length=100)
    crop = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    price_per_kg = models.FloatField()

    def __str__(self):
        return self.name

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    required_crop = models.CharField(max_length=50)
    preferred_region = models.CharField(max_length=50)
    budget = models.FloatField()

    def __str__(self):
        return self.name
