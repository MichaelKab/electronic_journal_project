from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404

def index(request):
	return HttpResponse('Надеюсь заработает!')
# Create your views here.
