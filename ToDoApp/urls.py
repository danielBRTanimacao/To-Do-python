from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_view, name='create'),
    path('logout/', views.logout_view, name='logout'),
    path('task/<str:name>/<int:id>/',  views.task_view, name='task'),
    path('delete/task/<int:id>/',  views.delete_task, name='delete_task')
]
