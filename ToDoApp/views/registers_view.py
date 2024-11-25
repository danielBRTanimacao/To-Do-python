from django.shortcuts import render, redirect
from ToDoApp.forms import RegisterForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    
    context = {
        'title': 'Login',
        'form': form
    }

    return render(request, 'pages/login.html', context)

def create_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    
    context = {
        'title': 'Registrar',
        'form': form
    }

    return render(request, 'pages/create.html', context)

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('index')