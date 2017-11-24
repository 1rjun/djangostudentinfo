from django.db import models

# Create your models here.

class Class(models.Model):
    Sem = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Dob = models.DateField()
    
    def __str__(self):
        return self.Sem

class Student(models.Model):
    Rollno = models.IntegerField(unique=True)
    Semester = models.ForeignKey(Class)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Rollno)