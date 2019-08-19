from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):

    title = models.CharField(verbose_name="Title", max_length=50)
    slug = models.SlugField(verbose_name="Slug", max_length=200, db_index=True, unique=True, default=None)
    description = models.CharField(verbose_name='Description', max_length=250)

    class Meta:
        ordering = ["title"]
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Course(models.Model):

    title = models.CharField(verbose_name="Title", max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, default=None)
    category = models.ForeignKey(Category, verbose_name="Category", related_name="category", on_delete=models.CASCADE)
    short_description = models.CharField(verbose_name="Short description", max_length=250)
    long_description = models.TextField(verbose_name="Long description")
    icons = models.ImageField(upload_to='', height_field=None, width_field=None, max_length=100)
    price = models.DecimalField(verbose_name="Price", max_digits=8, decimal_places=2)
    date_start = models.DateField(verbose_name="Date start", auto_now=False, auto_now_add=False)
    date_end = models.DateField(verbose_name="Date end", auto_now=False, auto_now_add=False)
    teacher = models.ManyToManyField("Teacher", verbose_name="Teacher", related_name="teacher", blank=True)
    student = models.ManyToManyField(User, verbose_name="User", related_name='courses', blank=True)

    class Meta:
        ordering = ["date_start"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Course_detail", kwargs={"pk": self.pk})


class Lesson(models.Model):

    title = models.CharField(verbose_name="Title", max_length=50)
    course = models.ForeignKey(Course, verbose_name="Course", related_name="lessons", on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Description", max_length=50)
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=False)
    duration = models.PositiveSmallIntegerField("Duration")
    homework = models.TextField(verbose_name="Home work")
    finished = models.BooleanField(verbose_name="Finished", default=False)

    class Meta:
        ordering = ["date"]
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Lesson_detail", kwargs={"pk": self.pk})


class Teacher(models.Model):

    first_name = models.CharField(verbose_name="First name", max_length=50)
    last_name = models.CharField(verbose_name="Last name", max_length=50)
    info = models.TextField(verbose_name="Information")

    class Meta:
        ordering = ["first_name"]
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("Teacher_detail", kwargs={"pk": self.pk})


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", blank=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
