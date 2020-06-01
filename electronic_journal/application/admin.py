from django.contrib import admin
from .models import lesson, daily_timetable, classes, Users
import uuid 
admin.site.register(lesson)
admin.site.register(Users)
admin.site.register(classes)

class daily_timetable_Admin(admin.ModelAdmin):
    list_display = ('Day', 'number_of_lessons','lessons')
    list_filter = ('Day', 'number_of_lessons', 'lessons')
admin.site.register(daily_timetable, daily_timetable_Admin)