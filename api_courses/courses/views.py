from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def CoursesView(request):
    return HttpResponse('<h1>Hello ToDo List!</h1>')
