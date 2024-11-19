from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ToDoApp.urls')),
    path('admin/', admin.site.urls),
]
