from venv import create
from django.db import models

# Create your models here.


class Task(models.Model):
   body = models.CharField(max_length=500)
   done = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True)