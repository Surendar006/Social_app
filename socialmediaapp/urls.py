from django.urls import path
from . import views

urlpatterns = [
    path('/signup', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('/logout', views.logout_view, name='logout'),
    path('/home', views.home_view, name='home'),
    path('post/create/', views.post_create_view, name='post_create'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('post/<int:post_id>/dislike/', views.dislike_post, name='dislike_post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
