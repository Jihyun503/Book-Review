from django.db import models

# Create your models here.
class Bestseller(models.Model):
    rank = models.IntegerField()
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=32)
    price = models.IntegerField()
    pub_date = models.CharField(max_length=10)
    bookcover = models.TextField()
    standard_week = models.CharField(max_length=6)