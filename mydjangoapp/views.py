from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Task
@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    context ={'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)

