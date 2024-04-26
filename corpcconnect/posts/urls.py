# posts/urls.py
from django.urls import path
from .views import get_profile, edit_profile, get_posts, create_post, view_pdf, like_post, dislike_post
app_name = 'posts'

urlpatterns = [
    path('profile/', get_profile, name='get_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('user/<str:user_id>/', get_posts, name='user_posts'),
    path('create/', create_post, name='create_post'),
    path('document/<int:document_id>/', view_pdf, name='view_pdf'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('dislike/<int:post_id>/', dislike_post, name='dislike_post'),
]

