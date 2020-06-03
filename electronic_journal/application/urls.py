from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name = 'index'),
	path("tes", views.tes, name = 'tes'),
]