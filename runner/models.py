from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=128)
    psd=models.CharField(max_length=16)
    studentId=models.CharField(max_length=10)

