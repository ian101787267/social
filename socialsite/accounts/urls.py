from django.urls import path
from .views import signup, create_post, create_comment, send_friend_request, accept_friend_request, home, login_view, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('create_post/', create_post, name='create_post'),
    path('post/<int:post_id>/comment/', create_comment, name='create_comment'),
    path('send_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('accept_request/<int:request_id>/', accept_friend_request, name='accept_friend_request'),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
