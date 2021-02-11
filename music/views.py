from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AlbumRatingUpdateForm
from .models import Genre, Album
from users.models import AlbumRating
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


def show_album(request, pk):
	album = get_object_or_404(Album, pk=pk)
	album_rating = AlbumRating.objects.filter(profile=request.user.profile, album=album).first()

	if album_rating is None:
		album_rating = AlbumRating()

	if request.method == 'POST':
		ar_form = AlbumRatingUpdateForm(request.POST)
		if ar_form.is_valid():
			form_data = ar_form.save(commit=False)
			album_rating.star_review = form_data.star_review
			album_rating.private_notes = form_data.private_notes
			album_rating.album = album
			album_rating.profile = request.user.profile
			album_rating.save()
			messages.success(request, f'Updated')
			return HttpResponseRedirect(request.path_info)
	else:
		ar_form = AlbumRatingUpdateForm(instance=album_rating)


	context = {
		'album': album,
		# 'rating': rating,
		'ar_form': ar_form
	}
	return render(request, 'music/album.html', context)

def my_music(request):
	album_ratings = AlbumRating.objects.filter(profile=request.user.profile)
	ratings = list()
	rating = dict()

	for album_rating in album_ratings:
		if album_rating.private_notes:
			notes = album_rating.private_notes
		else:
			notes = 'No notes for this album'

		rating = {
			'album': album_rating.album,
			'notes': notes,
			'stars': range(album_rating.star_review),
			'blankstars': range(album_rating.star_review, 5)
		}
		ratings.append(rating)

	context = {
		'ratings': ratings
	}
	return render(request, 'music/my_music.html', context)