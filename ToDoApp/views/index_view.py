from django.shortcuts import render, redirect
from ToDoApp.models import Task
from ToDoApp.task_form import TaskForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    
    tasks = Task.objects.all()
    form = TaskForm()

    context = {
        'title': 'index',
        'tasks': tasks,
        'form': form
    }
    return render(request, 'pages/index.html', context)
