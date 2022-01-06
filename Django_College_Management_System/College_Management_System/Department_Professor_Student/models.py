from django.db import models

# Create your models here.

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True,auto_created=True)
    department_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.department_id},{self.department_name},{self.subject}"

class Professor(models.Model):
    department_id = models.ManyToManyField(Department,related_name='department_pro')
    Professor_name = models.CharField(max_length=50)
    salary = models.FloatField()

    def __str__(self):
        return f"{self.department_id},{self.Professor_name},{self.salary}"

class Student(models.Model):
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='department_stud')
    roll_no = models.IntegerField()
    name = models.CharField(max_length=50)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.department_id},{self.roll_no},{self.name},{self.marks}"