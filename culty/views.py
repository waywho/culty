from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	# return HttpResponse('home')
	return render(request, 'homepage.html')

def about(request, slug):
	# return HttpResponse('about')
	return render(request, 'about.html')