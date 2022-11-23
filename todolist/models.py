from django.db import models


# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=1000)
    Date = models.DateField(blank=False)
    completed= models.BooleanField()

    def __str__(self):
        return self.task
