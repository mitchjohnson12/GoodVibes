from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, FriendRequest

###
# Logins/Proviles
###
def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created!')
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', context={'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
									request.FILES, 
									instance=request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated')
			return redirect('profile')


	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
		'u_form': u_form,
		'p_form': p_form
	}

	return render(request, 'users/profile.html', context)


###
# Friends Pages
###
@login_required
def friends_search(request):
	user_list = User.objects.exclude(id=request.user.id).order_by('last_name', 'first_name', 'username')
	my_friends = request.user.profile.friends.all().values_list('user', flat=True)
	requested_me_users = FriendRequest.objects.filter(to_user=request.user).values_list('from_user', flat=True)
	my_pending_request_users = FriendRequest.objects.filter(from_user=request.user).values_list('to_user', flat=True)
	
	context_list = list() # user, button_type, button_caption
	
	for user in user_list:
		if user.id in my_friends:
			button_type = 'info disabled'
			button_caption = 'Already Friends <3'
			button_url = None

		elif user.id in requested_me_users:
			button_type = 'success'
			button_caption = 'Accept Request'
			button_url = '/users/acceptrequest/'

		elif user.id in my_pending_request_users:
			button_type = 'warning'
			button_caption = 'Cancel Request'
			button_url = '/users/cancelrequest/'

		else:
			button_type = 'primary'
			button_caption = 'Send Request'
			button_url = '/users/sendrequest/'

		context_list.append((user, button_type, button_caption, button_url))

	context = {
		'context_list': context_list
	}

	return render(request, 'users/friends_search.html', context)
	


def profile_pk(request, pk):
	user = get_object_or_404(User, pk=pk)

	context = {
		'user': user
	}
	return render(request, 'users/profile_pk.html', context)




@login_required
def my_friends(request):
	sent_friend_requests = FriendRequest.objects.filter(from_user=request.user)
	received_friend_requests = FriendRequest.objects.filter(to_user=request.user)
	friends = request.user.profile.friends.all()

	# TODO - Add stuff for buttons

	context = {
		'friends': friends,
		'sent_friend_requests': sent_friend_requests,
		'received_friend_requests': received_friend_requests
	}

	return render(request, 'users/my_friends.html', context)


###
# Friend Requests
###
# Functions for sending friend requests
@login_required
def send_friend_request(request, pk):
	to_user = get_object_or_404(User, pk=pk)
	friend_request, created = FriendRequest.objects.get_or_create(
		from_user=request.user,
		to_user=to_user
		)
	return redirect('users-friendsearch')


@login_required
def cancel_friend_request(request, pk):
	to_user = get_object_or_404(User, pk=pk)
	friend_request = FriendRequest.objects.filter(
		from_user=request.user,
		to_user=to_user
		).first()
	if friend_request:
		friend_request.delete()
	return redirect('users-friendsearch')


# Functions for responding to friend requests
@login_required
def accept_friend_request(request, pk):
	from_user = get_object_or_404(User, pk=pk)
	to_user = request.user
	friend_request = FriendRequest.objects.filter(
		from_user=from_user,
		to_user=to_user
		).first()
	if friend_request:
		to_user.profile.friends.add(from_user.profile)
		from_user.profile.friends.add(to_user.profile)
		friend_request.delete()
		return redirect(f'/users/{from_user.id}')
	else:
		return redirect('users-friendsearch')


@login_required
def delete_friend_request(request, pk):
	from_user = get_object_or_404(User, pk=pk)
	friend_request = FriendRequest.objects.filter(
		from_user=from_user,
		to_user=request.user
		)
	friend_request.delete()
	return redirect('home-homepage')

