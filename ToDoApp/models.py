from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)
    date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)