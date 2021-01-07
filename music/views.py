from django.shortcuts import render, get_object_or_404
from .models import Genre, Album
from django.db.models import Count


def home(request):
	context = {
			'application': 'music'
	}
	return render(request, 'home/under_construction.html', context)


def explore_all(request):
	genre_list = Genre.objects.all()
	#genre_count = Album.objects.values('genre').order_by('genre').annotate(count=Count('id'))
	context = {
			'application': 'music',
			'genre_list': genre_list
	}
	return render(request, 'music/explore.html', context)


def explore_genre(request, pk):
	genre = get_object_or_404(Genre, pk=pk)
	album_list = Album.objects.filter(genre=genre.id).order_by('primary_artist__name')
	context = {
		'genre': genre,
		'album_list': album_list
	}
	return render(request, 'music/genre.html', context)
