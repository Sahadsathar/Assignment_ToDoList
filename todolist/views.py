from django.shortcuts import render, redirect
from . models import *
from django.utils.datastructures import MultiValueDictKeyError

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
def complete(request):
    pass