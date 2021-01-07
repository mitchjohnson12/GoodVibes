# need to run in shell

from music.models import Genre, Artist, Album
import csv

path = r'sample library data/album_test_import.csv'

with open(path) as file:
	albums_reader = csv.reader(file)
	next(albums_reader)
	for row in albums_reader:
		genre = Genre.objects.get(name=row[3])
		artist, created = Artist.objects.get_or_create(name=row[2])
		_, created = Album.objects.get_or_create(
			year=row[0], 
			title=row[1],
			primary_artist=artist,
			genre=genre
			)

