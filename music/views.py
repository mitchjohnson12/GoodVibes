from django.shortcuts import render


def home(request):
	context = {
			'application': 'music'
	}
	return render(request, 'home/under_construction.html', context)
