from django.db import models


# Create your models here.
class Check(models.Model):
    compleated = models.CharField(max_length=30)

    def __str__(self):
        return self.compleated


class Todo(models.Model):
    created_by = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    compleated = models.ForeignKey(Check, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.created_by

