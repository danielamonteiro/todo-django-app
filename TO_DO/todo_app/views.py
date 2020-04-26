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

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário e/ou senha inválido (s)!")

        return redirect('/')

@login_required(login_url='/login/')
def tasks_list(request):
    user_task = request.user
    task = Tasks.objects.filter(task_user=user_task)
    data = {'tasks': task}

    return render(request, 'todo.html', data)

@login_required(login_url='/login/')
def task(request):
    id_task = request.GET.get('id')
    data = {}
    if id_task:
        data['task'] = Tasks.objects.get(id=id_task)
    
    return render(request, 'task.html', data)

@login_required(login_url='/login/')
def submit_task(request):
    if request.POST:
        task_name = request.POST.get('task_name')
        cetegory = request.POST.get('category')
        description = request.POST.get('description')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        task_user = request.POST.get('task_user')
        id_task = request.POST.get('id_task')
        if id_task:
            task = Tasks.objects.get(id=id_task)
            if task.user_task == task_user:
                task.task_name = task_name
                task.category = category
                task.description = description
                task.deadline = deadline
                task.status = status
                task.save()
        else:
            Tasks.objects.create(task_name=task_name,
                                category=category,
                                description=description,
                                deadline=deadline,
                                status=status,
                                task_user=task_user)
        
    return redirect('/')

@login_required(login_url='/login/')
def delete_task(request, id_task):
    task_user = request.user
    try:
        task = Tasks.objects.get(id=id_task)
    except Exception:
        raise Http404
    if task_user == task.user_task:
        task.delete()
    else:
        raise Http404

    return redirect('/')



