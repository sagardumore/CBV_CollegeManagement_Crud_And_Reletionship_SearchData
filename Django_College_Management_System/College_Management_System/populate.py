import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'College_Management_System.settings')
django.setup()

from faker import Faker
import random
from Department_Professor_Student.models import Department,Professor,Student


dept_list = list(Department.objects.all())
fake = Faker()

def generateStudentData(n):
    for i in range(n):
        name = fake.name()
        roll_no = random.randint(10,100)
        marks = random.randint(10,100)
        department = random.choice(dept_list)
        department = fake.random_element(dept_list)
        student_obj = Student.objects.create(name=name,roll_no=roll_no,marks=marks,department_id=department)


generateStudentData(10)

def generateProfessorData(n):
    for i in range(n):
        Professor_name = fake.name()
        salary = random.randint(5,100)
        l = random.randint(2,4)
        department = fake.random_elements(dept_list,length=l,unique=True)
        professor_obj = Professor.objects.create(Professor_name=Professor_name,salary=salary)
        professor_obj.department_id.set(department)

generateProfessorData(10)