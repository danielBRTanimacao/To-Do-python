from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100)
    due_date = models.DateTimeField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Task {self.user.username}"