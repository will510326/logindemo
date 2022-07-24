from django.shortcuts import get_object_or_404, redirect, render
from tenacity import retry
from .models import Todo
from .forms import TodoForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.


def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()

    return redirect('todo')


@login_required
def completed(request):
    todos = Todo.objects.filter(user=request.user, completed=True)
    return render(request, './todo/completed.html', locals())


@login_required
def create(request):
    form = TodoForm()
    message = ''
    try:
        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():  # form表單是否符合合法(設定標準)
                todo = form.save(commit=False)  # 因沒有user資訊，故先將commit=False先不儲存
                todo.user = request.user
                todo.save()  # 可以將資料儲存到資料庫
                return redirect('todo')
            else:
                message = '新增失敗'
    except Exception as e:
        print(e)
    return render(request, './todo/create.html', locals())


@login_required
def view(request, id):
    # todo = Todo.objects.filter(id=id)
    message = ''
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(instance=todo)  # 取的表單資訊
    if request.method == 'POST':
        if request.POST.get('delete'):
            todo.delete()
            return redirect('todo')

        if request.POST.get('update'):
            message = '更新失敗'
            try:
                form = TodoForm(request.POST, instance=todo)
                if form.is_valid():
                    todo = form.save(commit=False)
                    todo.date_completed = datetime.today().strftime('%Y-%m-%d %H:%M:%S')\
                        if todo.completed else None
                    todo.save()
                    return redirect('todo')
            except Exception as e:
                print(e)

    return render(request, './todo/view.html', locals())


def todo(request):
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
    print(todos)
    return render(request, './todo/todo.html', locals())
