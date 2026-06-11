from django.contrib import admin
from myapp.models import *
# Register your models here.

class DeptDisplay(admin.ModelAdmin):
    list_display = ['id','name']
    
class SubjectDisplay(admin.ModelAdmin):
    list_display=['id','name']
    
class StudentIdDisplay(admin.ModelAdmin):
    list_display = ['student_id']
    
class StudentDisplay(admin.ModelAdmin):
    list_display = ['st_id','dept_name','name','email','age','phone']
    
    def dept_name(self, obj):
        return obj.dept.name
    
    def st_id(self,obj):
        return obj.student_id.student_id
    
class MarksDisplay(admin.ModelAdmin):
    list_display = ['student_name','subject_name','marks']
    
    def student_name(self,obj):
        return obj.student.name
    
    def subject_name(self,obj):
        return obj.subject.name

admin.site.register(Dept,DeptDisplay)
admin.site.register(StudentId,StudentIdDisplay)
admin.site.register(Student,StudentDisplay)
admin.site.register(Subject,SubjectDisplay)
admin.site.register(Marks,MarksDisplay)
