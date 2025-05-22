# my_django/views.py

from django.shortcuts import render

def index(request):
    # 模拟的待办事项
    todo_items = [
        'Wake up ☀️',
        'Hit the gym 💪',
        'Study 📚',
    ]
    
    return render(request, 'index.html', {'todo_items': todo_items})  # 渲染 index.html 模板
