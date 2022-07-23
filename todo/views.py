from django.shortcuts import get_object_or_404, render
from .models import Todo
# Create your views here.


def view(request, id):
    # todo = Todo.objects.filter(id=id)
    todo = get_object_or_404(Todo, id=id)
    return render(request, './todo/view.html', locals())


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    print(todos)
    return render(request, './todo/todo.html', locals())
