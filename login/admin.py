from django.contrib import admin
from .models import Student, Subject, Enrollment

# Register your models here.

class StudentEnrollment(admin.TabularInline):
    model = Enrollment

@admin.register(Student)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [StudentEnrollment]

@admin.register(Subject)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentEnrollment]
