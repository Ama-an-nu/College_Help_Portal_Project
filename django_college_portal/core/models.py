from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField(default=3)
    semester = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} (Sem {self.semester})"


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.designation}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    enrollment_id = models.CharField(max_length=20, unique=True)
    year = models.PositiveIntegerField()  # e.g., 1st, 2nd year

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.enrollment_id})"



class Placement(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    package = models.CharField(max_length=50)  # e.g., "6 LPA"
    eligibility = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.company} - {self.role}"


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateTimeField()
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.date.date()})"


class StudyRoadmap(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField(help_text="Steps, guidelines, or topics to cover")

    def __str__(self):
        return f"Roadmap for {self.course.title}"


class Resource(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to="resources/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
