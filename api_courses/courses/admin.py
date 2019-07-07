from django.contrib import admin
from courses.models import Category, Course, Lesson, Teacher


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "date_start"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "finished"]
    list_editable = ["finished"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["last_name"]
