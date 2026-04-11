class Student:

    def __init__(self,id,name,email):
        self.id = id
        self.name = name
        self.email=email

    def display(self):
        print(self.id,self.name,self.email)

s = Student(10,"krish","krish@gmail.com")
s.display()

s1 = Student(20,"Priyanshu","priyanshu@gmail.com")
s1.display()