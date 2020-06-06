from django.db import models
import datetime
class Users(models.Model):
	"""
	Model representing a book genre (e.g. Science Fiction, Non Fiction).
	"""
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	STATUS = (('s','student'),('t','teacher'))
	status = models.CharField(max_length=7, choices=STATUS, blank=True, default='student')
	#if status == 'student':
	#	level = models.ManyToManyField(classes, help_text="выберете класс")

	def __str__(self):
		return "{} {} {}".format(self.last_name,self.name, self.middle_name)

class lesson(models.Model):
	title = models.CharField(max_length=30, help_text="Урок")
	def __str__(self):
		return  self.title

class daily_timetable(models.Model):
	list_Days = (
		("Пн","Понедельник"),
		("Вт","Вторник"),
		("Ср","Среда"),
		("Чт","Четверг"),
		("Пт","Пятница"),
		("Сб","Суббота"),
		("Вс","Воскресенье")

	)
	Day = models.CharField(max_length=11, choices=list_Days, help_text="выберете день",default= datetime.date.today())
	date = models.DateTimeField(null=True, blank=True)#, default=datetime.timezone)
	number_of_lessons = models.CharField(max_length=1, help_text="Количество уроков")
	#for i in range(number_of_lessons.text()):
	lessons = models.CharField(max_length=200, help_text="выберете уроки")
	#lessons = models.ManyToManyField(lesson, help_text="выберете уроки")
	#number_of_lessons = len(lessons)
	def __str__(self):
		return  "{} {} {}".format(self.lessons, self.number_of_lessons, self.date)

class timetable(models.Model):
	date = models.DateField(null=True, blank=True)

#class day_lesson():

class classes(models.Model):
	PRE_Students_list = Users.objects.all().filter(status='s')
	Students_list = []
	for student in PRE_Students_list:
		Students_list.append((student,student))
	'''
	classes = [
	(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8),
	(9, 9),
	(10, 10),
	(11, 11)]
	'''
	grade = models.CharField(max_length = 4, help_text = "класс")
	#the_letter_class = models.CharField(max_length=1, help_text="буква класса")
	students = models.CharField(max_length = 100, choices = Students_list, help_text="выберите учеников", default = '')
	def __str__(self):
		return  '{}'.format(self.grade)

class Home_work(models.Model):
	date_start = models.DateTimeField(null=True, blank=True)
	deadline = models.DateTimeField(null=True, blank=True)
	text = models.CharField(max_length=100, help_text="текст ДЗ")
	for_class = models.ManyToManyField(classes, help_text="выберете класс")
	materials = models.FileField(upload_to=None, max_length=100)
	school_lesson = models.ManyToManyField(lesson, help_text="выберете урок")

	def __str__(self):
		return  '{} {}'.format(self.school_lesson,self.for_class)

class score(models.Model):
	PRE_Students_list = Users.objects.all().filter(status = 's')
	Students_list = []
	for student in PRE_Students_list:
		Students_list.append((student,student))
	'''
	teachers_list = []
	PRE_teachers_list = Users.objects.all().filter(status = 't')
	for teacher in PRE_teachers_list:
		teachers_list.append((teacher,teacher))
	'''
	# Проблема с teacher || ValueError: Cannot serialize: ...
	mark = models.CharField(max_length=3, help_text="оценка")
	teacher = models.CharField(max_length= 100,choices=Students_list, help_text="учитель",default= "")
	student = models.CharField(max_length= 100,choices=Students_list, help_text="ученик",default= "")
	school_subject = models.ManyToManyField(lesson, help_text="урок")
	def __str__(self):
		return  self.mark,self.school_subject