from django.shortcuts import render

def home(request):
	context = {
			'application': 'books'
	}
	return render(request, 'home/under_construction.html', context=context)
