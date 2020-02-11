from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	# return render(request, '../templates/base.html')
	return render(request, 'base.html')

def test(request):
	return render(request, 'test.html')

def courses(request):
	return render(request, 'courses.html')

def team(request):
	return render(request, 'team.html')

def profile(request):
	return render(request, 'profile.html')