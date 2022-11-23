from django.shortcuts import render, redirect
from django.template import RequestContext
from . models import *

def index(request):
    todo= Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            task = request.POST['task']
        )
        new_todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todos':todo})
def delete(request):
    pass