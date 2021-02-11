from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Genre(models.Model):
	name = models.CharField(max_length=20)
	image = models.ImageField(default='music_genres/default.jpg', upload_to='music_genres')

	def __str__(self):
		return self.name


class Album(models.Model):
	title = models.CharField(max_length=120)
	year = models.IntegerField()
	primary_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	genre = models.ForeignKey(Genre, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return f'{self.title} - {self.primary_artist.name} ({self.year})'
