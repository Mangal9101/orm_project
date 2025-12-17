from django.contrib import admin
from .models import Student

# Register your models here.

class Student_Admin(admin.ModelAdmin):
    list_display=['roll_no','name','course','fee','contact','address']

admin.site.register(Student,Student_Admin)
