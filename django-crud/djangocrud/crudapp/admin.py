from django.contrib import admin
from .models import Student
from .models import Teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    
    
    admin.site.register(Teacher)

