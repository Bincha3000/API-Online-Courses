from django.http import HttpResponse
from django.shortcuts import render


def CoursesView(request):
    return HttpResponse('<h1>Hello ToDo List!</h1>')
