from django.db import models
from django.db.models.fields import CharField

class object_return_data(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(title__contains='f')

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    book_object  = models.Manager()
    custome_filter_module_objects = object_return_data()


class common(models.Model):  # COMM0N
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Student(common):
    rollno = models.IntegerField()

class Teacher(common):
    class_name = None

