from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    year = models.IntegerField()
    student_id = models.IntegerField()

    def __str__(self):
        return f"{self.student_id} : {self.name} {self.surname}"

class Subject(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)
    semester = models.IntegerField()
    year = models.IntegerField()
    seats = models.IntegerField()
    
    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        FULL = 'FULL', 'Full'

    status = models.CharField(
        max_length=10,
        choices=Status.choices, 
        default="AVAILABLE" 
  
    )

    def __str__(self):
        return f"{self.code} {self.name} ({self.semester}/{self.year})"


    
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.student} ลงทะเบียน {self.subject}"
    
