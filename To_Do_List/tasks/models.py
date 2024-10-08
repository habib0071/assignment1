from django.db import models

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=33)
    taskDescription = models.CharField(max_length=500)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.taskTitle