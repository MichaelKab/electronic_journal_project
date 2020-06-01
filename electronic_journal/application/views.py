from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import daily_timetable
def index(request):
	timetable = daily_timetable.objects.order_by('date')
	return render(request, 'list.html',{"timetable": timetable})
# Create your views here.
