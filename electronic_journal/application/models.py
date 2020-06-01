from django.db import models

class Users(models.Model):
	"""
	Model representing a book genre (e.g. Science Fiction, Non Fiction).
	"""
	name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	STATUS = (('s','student'),('t','teacher'))
	classes = [1,2,3,4,5,6,7,8,9,10,11]
	status = models.CharField(max_length=7, choices=STATUS, blank=True, default='student')
	if status == 'student':
		level = models.ManyToManyField(classes, help_text="выберете класс")

	def __str__(self):
		return  self.last_name,self.name, self.middle_name

class lesson(models.Model):
	title = models.CharField(max_length=30, help_text="Урок")
	def __str__(self):
		return  self.title

class daily_timetable(models.Model):
	date = models.DateTimeField(null=True, blank=True)
	number_of_lessons = models.CharField(max_length=1, help_text="Количество уроков")
	lessons = models.ManyToManyField(lesson, help_text="выберете уроки")
	#number_of_lessons = len(lessons)
	def __str__(self):
		return  self.date, self.number_of_lessons, self.lessons

class timetable(models.Model):
	date = models.DateField(null=True, blank=True)

class classes(models.Model):
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
	(11, 11)
	]
	grade = models.CharField(max_length=1, choices=classes, help_text="выберете класс")
	the_letter_class = models.CharField(max_length=1, help_text="буква класса")
	students = models.ManyToManyField(Users, help_text="выберите учеников")
	def __str__(self):
		return  '{}{}'.format(self.grade,self.the_letter_class)

# Create your models here.
