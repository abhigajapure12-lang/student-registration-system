from django.contrib import admin
from .models import Student, Department, Course


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    search_fields = ['department_name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'duration']
    search_fields = ['course_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'email', 'phone', 'department', 'course']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_filter = ['department', 'course', 'age']
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'age', 'email', 'phone')
        }),
        ('Academic Information', {
            'fields': ('department', 'course')
        }),
    )

