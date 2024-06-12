from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PostForm, CommentForm, CustomAuthenticationForm
from .models import Post, Comment, FriendRequest, CustomUser

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.last_login = timezone.now()
            user.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            user.last_login = timezone.now()
            user.save()
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def create_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form, 'post': post})

@login_required
def send_friend_request(request, user_id):
    to_user = CustomUser.objects.get(id=user_id)
    friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    return redirect('home')

@login_required
def accept_friend_request(request, request_id):
    friend_request = FriendRequest.objects.get(id=request_id)
    if friend_request.to_user == request.user:
        friend_request.accepted = True
        friend_request.save()
        request.user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(request.user)
    return redirect('home')

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    users = CustomUser.objects.exclude(id=request.user.id) if request.user.is_authenticated else CustomUser.objects.all()
    friend_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False) if request.user.is_authenticated else None
    friends = request.user.friends.all() if request.user.is_authenticated else None
    return render(request, 'home.html', {'posts': posts, 'users': users, 'friend_requests': friend_requests, 'friends': friends})

def logout_view(request):
    logout(request)
    return redirect('home')
