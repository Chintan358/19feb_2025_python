from django.db import models

class Dept(models.Model):
    name = models.CharField(max_length=20)
    
class StudentId(models.Model):
    student_id = models.CharField(max_length=20)
    
class Student(models.Model):
    student_id = models.OneToOneField(StudentId,on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    
class Subject(models.Model):
    name = models.CharField(max_length=20)
    
class Marks(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    marks = models.FloatField()
    