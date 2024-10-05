from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    year = models.IntegerField()
    student_id = models.IntegerField()

    def __str__(self):
        return f"{self.student_id} : {self.name} {self.surname}"