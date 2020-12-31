from django.shortcuts import render

def home(request):
	context = {
			'application': 'movies'
	}
	return render(request, 'home/base.html', context=context)
