from django.contrib import admin
from home.models import Book , Student , Teacher



@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ['id','title','description','price']

@admin.register(Student)
class Student(admin.ModelAdmin):
    list_display = ['id','name','class_name','rollno']

@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ['id','name']