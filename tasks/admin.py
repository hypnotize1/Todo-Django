from django.contrib import admin
from .models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'due_date', 'priority', 'is_complete')
    list_filter =  ('priority', 'is_complete')
    search_fields = ('title', 'description')

