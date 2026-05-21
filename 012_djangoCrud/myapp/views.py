from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        data =request.POST
        name= data.get("name")
        email = data.get("email")
        age = data.get("age")
        Student.objects.create(name=name,email=email,age=age)
        return render(request,"index.html",{"msg":"Registration success !!!"})

def display(request):
    students = Student.objects.all()
    return render(request,"display.html",{"students":students})

def delete_students(request):
    id = request.GET.get('id')
    student= Student.objects.get(id=id)
    student.delete()
    return redirect("display")

def edit_student(request):
    id = request.GET.get('id')
    student= Student.objects.get(id=id)
    if request.method=='POST':
        data =request.POST
        name= data.get("name")
        email = data.get("email")
        age = data.get("age")
        student.name=name
        student.email = email
        student.age = age
        student.save()
        return render(request,"update.html",{"msg":"Update success !!!"})

    
    return render(request,"update.html",{"student":student})