from django.db import models
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    produce = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    required_crop = models.CharField(max_length=50)
    preferred_region = models.CharField(max_length=50)
    budget = models.FloatField()

    def __str__(self):
        return self.name
