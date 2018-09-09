from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    addr = models.CharField(max_length=80)
    # def __str__(self):
    #     return self.name