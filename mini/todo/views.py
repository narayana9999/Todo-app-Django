from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# Create your views here.

class TodoListview(ListView):
    model = Todo
    template_name = "todo/list.html"
    context_object_name = "todos"
    
class TodoCreateList(CreateView):
    model = Todo
    template_name = "todo/create.html"
    fields = ['title', 'description', 'is_active']
    success_url = reverse_lazy("todo_list")
    
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/update.html'
    fields = ['title', 'description', 'is_active']
    success_url = reverse_lazy("todo_list")
    
class TodoDeleteView(DeleteView):
    model = Todo
    template_name = "todo/delete.html"
    success_url = reverse_lazy("todo_list")