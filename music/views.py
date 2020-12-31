from django.shortcuts import render


def home(request):
	context = {
			'application': 'music'
	}
	return render(request, 'home/base.html', context)
