from django.shortcuts import render
from . models import *
from rest_framework import generics

# Create your views here.
# CRUD operation
class ListTodo(generics.ListAPIView):   # Read
    queryset=Todo.objects.all()

class DetailTodo(generics.RetrieveUpdateAPIView): # Update
    queryset = Todo.objects.all()

class CreateTodo(generics.CreateAPIView):  # Create
    queryset = Todo.objects.all()

class DeleteTodo(generics.DestroyAPIView): # Delete
    queryset = Todo.objects.all()


def index(request):
    return render(request, 'index.html')