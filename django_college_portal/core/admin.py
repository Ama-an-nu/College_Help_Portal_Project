from django.contrib import admin
from .models import Department, Course, Faculty, Student, Placement, Event, StudyRoadmap, Resource

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "credits", "semester")
    list_filter = ("department", "semester")
    search_fields = ("title",)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ("user", "department", "designation")
    list_filter = ("department",)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user", "enrollment_id", "department", "year")
    list_filter = ("department", "year")
    search_fields = ("user__username", "enrollment_id")

@admin.register(Placement)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ("company", "role", "package", "date")
    list_filter = ("company", "date")
    search_fields = ("company", "role")

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "department")
    list_filter = ("date", "department")
    search_fields = ("title",)

@admin.register(StudyRoadmap)
class StudyRoadmapAdmin(admin.ModelAdmin):
    list_display = ("course",)
    search_fields = ("course__title",)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_by", "uploaded_at")
    list_filter = ("uploaded_at",)
    search_fields = ("title",)
