from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Todo
from .forms import TodoForm


class TodoView(generic.ListView):
    template_name = "todo_app/todos.html"
    context_object_name = "todo_list"

    def get_queryset(self):
        """
        Возвращает все объекты модели Todo
        """
        return Todo.objects.all().order_by('pk')


class TodoUpdateView(generic.UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo_app/todo_edit.html'
    success_url = reverse_lazy('todo_app:todos')


def todo_create(request):
    """
    Форма создания todo
    """
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app:todos')
    form = TodoForm()
    return render(request, 'todo_app/todo_create.html', {'form': form})


def delete(request, *args, **kwargs):
    """
    Удаляет записи по списку чекбоксов todo_id 
    """
    selected_todos = request.POST.getlist('selected_todos')
    Todo.objects.filter(id__in=selected_todos).delete()
    return redirect('todo_app:todos')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo_app:todos')
        else:
            messages.error(request, 'Неверные учетные данные.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('todo_app:login')
