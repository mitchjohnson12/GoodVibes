from django import forms
from users.models import AlbumRating

class AlbumRatingUpdateForm(forms.ModelForm):
	class Meta:
		model = AlbumRating
		fields = ['star_review', 'private_notes']