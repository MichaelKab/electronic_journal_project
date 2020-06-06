from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import daily_timetable,Users
import string
def index(request):
	days_short = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
	days_long = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
	
	timetable = daily_timetable.objects.order_by('date')
	#days = []
	for a in timetable:
		a.lessons = a.lessons.split(",")
		a.Day = days_long[days_short.index(a.Day)]
		a.date = '.'.join(str(a.date).split(" ")[0].split('-')[1:3])
#		days.append(days_long[days_short.index(x.Day)])
	return render(request, 'list.html',{"timetable": timetable,})
# Create your views here.
def tes(request):
	days_short = ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"]
	days_long = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
	timetable = daily_timetable.objects.order_by('date')
	lessons_in_day = []
	days = []
	for a in timetable:
		#lessons_in_day.append(a.lessons)
		a.lessons = a.lessons.split(",")
		lessons_in_day.append(a)
	for x in timetable:
		days.append(days_long[days_short.index(x.Day)])
	#return HttpResponse(lessons_in_day[0].split(','))
	return HttpResponse(lessons_in_day)#[0].lessons[0])
	#return HttpResponse(Users.objects.all().filter(status='s'))