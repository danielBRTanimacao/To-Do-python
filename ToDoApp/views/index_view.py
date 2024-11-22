from django.shortcuts import render, redirect
from models import Task

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    
    tasks = Task.objects.all()

    context = {
        'title': 'index',
        'tasks': tasks
    }
    return render(request, 'pages/index.html', context)
