from django.shortcuts import render

def home(request):
	context = {
			'application': 'books'
	}
	return render(request, 'home/base.html', context=context)
