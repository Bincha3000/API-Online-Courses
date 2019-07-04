from django.urls import path

from .views import CoursesView

app_name = 'courses'
urlpatterns = [
    path('courses/', CoursesView)
]
