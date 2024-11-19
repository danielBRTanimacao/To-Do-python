from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = []
    ordering = []
    search_fields = []
    list_editable = []
    list_per_page = 10
    list_max_show_all = 150
    list_display_links = []