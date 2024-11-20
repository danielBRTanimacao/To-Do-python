from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'status', 'created']
    search_fields = ['id', 'user', 'title', 'created']
    list_display_links = ['id', 'user', 'title']
    list_per_page = 10
    list_max_show_all = 150