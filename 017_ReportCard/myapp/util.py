import faker
fake = faker.Faker()
import random
from myapp.models import *

def create(n=50):
    depts = Dept.objects.all()
    
    for i in range(n):
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        age = random.randint(21,30)
        stid = StudentId.objects.create(student_id=f"STD_{random.randint(100,999)}")
        dept = depts[random.randint(0,len(depts)-1)]
        

        Student.objects.create(student_id=stid,dept=dept,name=name,email=email,age=age,phone=phone)
        
        
def set_marks():
    students = Student.objects.all()
    subjects = Subject.objects.all()
    for student in students:
        for subject in subjects:
            Marks.objects.create(student=student,subject=subject,marks=random.randint(1,50))