from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student = models.ForeignKey(User,unique=True)
    semseter = models.CharField(max_length=50)
    Stream = models.CharField(max_length=50)
    Rollno = models.IntegerField()
    
    def __str__(self):
        return str(self.Rollno)

