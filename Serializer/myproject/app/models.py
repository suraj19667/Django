from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=15)