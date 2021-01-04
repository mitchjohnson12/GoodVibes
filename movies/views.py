from django.shortcuts import render

def home(request):
	context = {
			'application': 'movies'
	}
	return render(request, 'home/under_construction.html', context=context)
