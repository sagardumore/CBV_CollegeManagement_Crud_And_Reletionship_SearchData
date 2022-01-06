import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'College_Management_System.settings')
import django
django.setup()

from Department_Professor_Student.models import *

from faker import Faker
from random import *

fake = Faker()


def populate(n):
    for i in range(n):
        fname = fake.department_name()
        fsub = fake.subject()

        department_record = Department.objects.get_or_create(department_name=fname, subject=fsub)

populate(200)