from django.shortcuts import render, redirect
from ToDoApp.models import Task
from ToDoApp.task_form import TaskForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    
    tasks = Task.objects.filter(user=request.user)
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')

    context = {
        'title': 'index',
        'tasks': tasks,
        'form': form
    }
    return render(request, 'pages/index.html', context)
