from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('create_group/', views.create_group, name='create_group'),
    path('join_group/', views.join_group, name='join_group'),
    path('my_groups/', views.my_groups, name='my_group'),
    path('group_details/<int:variable_id>/', views.group_details, name='group_details'),
]