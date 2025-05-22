# my_django/views.py

from django.shortcuts import render

def index(request):
    # 模拟 To-Do list 数据
    todo_items = [
        'Wake up ☀️',
        'Hit the gym 💪',
        'Study 📚',
    ]
    
    # 渲染模板并传递数据
    return render(request, 'index.html', {'todo_items': todo_items})
