from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from ToDoApp.models import Task
from ToDoApp.task_form import TaskForm

@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user=request.user)
    paginator = Paginator(tasks, 10)
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'index',
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'pages/index.html', context)

@login_required(login_url='login')
def task_view(request, name, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'title': f'task de {name}',
        'form': form,
        'task': task
    }
    return render(request, 'pages/task.html', context)

@login_required(login_url='login')
def delete_task(request, id):
    task_delete = get_object_or_404(Task, id=id, user=request.user)
    task_delete.delete()
    return redirect('index')