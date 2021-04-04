from django.db import models

#To Do table
class Todo(models.Model):
    task = models.CharField(max_length = 100)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
