from django.contrib import admin
from .models import Category, Course, Lesson, Teacher

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "date_start"]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["name", "finished"]
    list_editable = ["finished"]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["last_name"]