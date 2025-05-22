# my_django/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # 导入 views 文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # 设置主页路由，指向 index 视图
]
