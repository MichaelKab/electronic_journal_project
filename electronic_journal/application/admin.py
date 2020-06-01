from django.contrib import admin
from .models import Users, lesson, daily_timetable, classes
admin.site.register(lesson)
admin.site.register(Users)
admin.site.register(daily_timetable)
admin.site.register(classes)
# Register your models here.
