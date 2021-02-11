from django.urls import path
from . import views

urlpatterns = [
		path('', views.home, name='music-home'),
		path('explore/<int:pk>', views.explore_genre, name='music-explore-genre'),
		path('explore/', views.explore_all, name='music-explore'),
		path('album/<int:pk>', views.show_album, name='music-album'),
		path('my-music', views.my_music, name='music-mymusic')
]


