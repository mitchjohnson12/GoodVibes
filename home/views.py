from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def homepage(request):
	context = {
			'application': 'home'
	}
	return render(request, 'home/under_construction.html', context=context)
