from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','description', 'link')


admin.site.register(Course,CourseAdmin)

