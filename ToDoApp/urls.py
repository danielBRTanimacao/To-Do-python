from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_view, name='create'),
    path('logout/', views.logout, name='logout'),
]
