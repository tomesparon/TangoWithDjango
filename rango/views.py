from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request): 
	html= "<h1>Rango says hey there parter</h1>" + '<br/><a href="/rango/about/">About</a>'
	return HttpResponse(html)

def about(request):

	abouthtml= "<h2>You are on the about page</h2>" + '<br/><a href="/rango/">Home</a>'
	return HttpResponse(abouthtml)