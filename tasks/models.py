from django.db import models
from users.models import *

# Create your models here.


class Task(models.Model):
    task_from = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tasks')
    task_to = models.ManyToManyField(User,related_name='tasks_given')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_at = models.DateTimeField()

    def __str__(self):
        return f"{self.description} -- {self.due_at}"