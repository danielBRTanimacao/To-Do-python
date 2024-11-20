from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'pages/index.html', {'title': 'index'})

def login_view(request):
    if request.method == "POST":
        pass

def create_view(request):
    return ...