from django.shortcuts import render, redirect
from todo_app.models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime
from django.http.response import Http404, JsonResponse

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    return redirect('/')

def tasks_list(request):
    user_task = request.user
    task = Tasks.objects.filter(task_user=user_task)
    data = {'tasks': task}

    return render(request, 'tasks.html', data)
