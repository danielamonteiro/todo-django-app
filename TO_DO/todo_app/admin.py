from django.contrib import admin
from todo_app.models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'task_name', 'deadline', 'task_user')
    list_filter = ('deadline',)

admin.site.register(Tasks, TasksAdmin)
