from django.db import models

# Create your models here.
class Schedule(models.Model):
    writer = models.ForeignKey('common.User', on_delete=models.CASCADE) #일정 등록한 사람의 id
    title = models.CharField(max_length=64) #책 제목
    contents = models.CharField(max_length=100, blank=True) #한마디
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
