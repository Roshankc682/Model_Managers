from django.shortcuts import render
from home.models import  Book




def list(request):
    context = {'form': "form","title":"Register"}
    context = Book.book_object.all()
    return render(request,'list.html',{"context":context})


def filter_list(request):
    context = {'form': "form","title":"Register"}
    context = Book.custome_filter_module_objects.all()
    return render(request,'filter_list.html',{"context":context})