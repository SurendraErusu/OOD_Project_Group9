from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('approve/<int:new_user_id>/', views.approve_user, name='approve_user'),
]

