from django.db import models

class Artist(models.Model):
	name = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.name


class Genre(models.Model):
	name = models.CharField(max_length=20)


class Album(models.Model):
	ROCK = 'RR'
	FUNK = 'FS'
	JAZZ = 'JZ'
	BLUES = 'LB'
	POP = 'PP'
	FOLK = 'FK'
	CLASSICAL = 'CL'
	RAGGAE = 'RG'
	HIPHOP = 'HH'
	ELECTRO = 'EL'
	LATIN = 'LT'
	GENRE_CHOICES = [
		(ROCK, 'Rock'),
		(FUNK, 'Funk / Soul'),
		(JAZZ, 'Jazz'),
		(BLUES, 'Blues'),
		(POP, 'Pop'),
		(FOLK, 'Folk'),
		(CLASSICAL, 'Classical'), 
		(RAGGAE, 'Reggae'), 
		(HIPHOP, 'Hip Hop'), 
		(ELECTRO, 'Electronic'), 
		(LATIN, 'Latin')
		]
	title = models.CharField(max_length=120)
	year = models.IntegerField()
	primary_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default=ROCK)

	def __str__(self):
		return f'{self.title} - {self.primary_artist.name} ({self.year})'

