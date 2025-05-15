from fabric import task, Connection

REPO_URL = 'https://github.com/yourname/yourproject.git'
REMOTE_DIR = '/home/ubuntu/myproject'
VENV_DIR = f'{REMOTE_DIR}/venv'

@task
def deploy(c):
    c = Connection(host='你的服务器IP', user='ubuntu')
    if not c.run(f'test -d {REMOTE_DIR}', warn=True).ok:
        c.run(f'git clone {REPO_URL} {REMOTE_DIR}')
    else:
        c.run(f'cd {REMOTE_DIR} && git pull')

    if not c.run(f'test -d {VENV_DIR}', warn=True).ok:
        c.run(f'python3 -m venv {VENV_DIR}')
    c.run(f'{VENV_DIR}/bin/pip install -r {REMOTE_DIR}/requirements.txt')

    c.run(f'{VENV_DIR}/bin/python {REMOTE_DIR}/manage.py collectstatic --noinput')
    c.run(f'{VENV_DIR}/bin/python {REMOTE_DIR}/manage.py migrate')
    c.run('sudo systemctl restart gunicorn')
