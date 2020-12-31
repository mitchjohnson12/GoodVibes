from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
	context = {
			'application': 'home'
	}
	return render(request, 'home/base.html', context=context)
