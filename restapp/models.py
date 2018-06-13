from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    task_desk = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now=True)
