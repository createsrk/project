from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=5000)

class Offer(models.Model):
    code = models.CharField(max_length=15)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
