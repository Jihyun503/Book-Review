from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=20, unique=True, primary_key=True)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=128, unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    registerDttm = models.DateTimeField(auto_now_add=True)
