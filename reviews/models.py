from atexit import register
from operator import mod
from unicodedata import category
from django.db import models

# Create your models here.

class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64)
    contents = models.TextField(verbose_name="내용")
    writer = models.ForeignKey('common.User', on_delete=models.CASCADE)
    category = models.CharField(max_length=32, db_index=True)
    write_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    hits = models.PositiveIntegerField(default=0)
    meta_json = models.TextField() # 별점이나 추가적으로 다른 데이터가 들어갈 때