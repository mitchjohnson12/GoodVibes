from django.urls import path
from . import views

urlpatterns = [
		path('<int:pk>', views.profile_pk, name='users-profilepk'),
		path('', views.my_friends, name='users-myfriends'),
		path('sendrequest/<int:pk>', views.send_friend_request, name='users-sendrequest'),
		path('acceptrequest/<int:pk>', views.accept_friend_request, name='users-acceptrequest'),
		path('cancelrequest/<int:pk>', views.cancel_friend_request, name='users-cancelrequest'),
]


