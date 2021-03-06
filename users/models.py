from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from music.models import Album
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')
	friends = models.ManyToManyField('Profile', blank=True)

	def __str__(self):
		return f'{self.user.username} profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)


class FriendRequest(models.Model):
	to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'from {self.from_user} to {self.to_user}'


class AlbumRating(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	star_review = models.IntegerField(
		null=True,
		validators=[
			MaxValueValidator(5),
			MinValueValidator(1)
		]
	)
	date_first_added = models.DateTimeField(auto_now_add=True)
	private_notes = models.TextField(max_length=1000)

