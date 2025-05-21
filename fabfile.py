from fabric import task
from invoke import env

# 设置远程主机用户名和地址
env.hosts = ['ubuntu@192.144.190.246']

@task
def deploy(c):
    # 拉取最新的代码
    c.run('git pull origin master')
    
    # 安装依赖
    c.run('pip install -r requirements.txt')
    
    # 迁移数据库
    c.run('python manage.py migrate')
    
    # 收集静态文件
    c.run('python manage.py collectstatic --noinput')
    
    # 重启 Gunicorn 和 Nginx
    c.run('sudo systemctl restart gunicorn')
    c.run('sudo systemctl restart nginx')
