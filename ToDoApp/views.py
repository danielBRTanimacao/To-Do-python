from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request, 'pages/index.html', {'title': 'index'})

def login_view(request):
    return ...

def create_view(request):
    return ...