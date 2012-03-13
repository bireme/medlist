# -*- coding: utf-8 -*-
from fabric.api import env, local, settings, abort, run, cd
from fabric.operations import local,put, sudo
from fabric.context_managers import prefix


def dev():
    env.user = ''
    env.hosts = ['']
    env.path = ''

 
def prod():    
    env.user = ''
    env.hosts = ['']
    env.path = ''

def reset_db(app):
    """Realiza reset do app
    """    
    with prefix('. PATH_TO_ENV'):
        with cd(env.path):   
            run('python manage.py reset %s --noinput' % app) 
            run('python manage.py syncdb')
            run('python manage.py loaddata fixtures/%s.json' % app)
     

def migration():
    """Realiza migration local
    """    
    with prefix('. PATH_TO_ENV'):
       local('python manage.py schemamigration gerenciador --auto') 
       local('python manage.py migrate gerenciador')

def restart_app():
    """Restarts remote uwsgi.
    """
    with cd(env.path):
        cd("..")
        run("touch production.wsgi")

def simple_update():
    """Somente atualiza código (git pull) e restart serviço
    """
    with cd(env.path):
        run("git pull")
    restart_app()
 
def full_update():    
    """Atualiza código. Instala dependências. Migrations. Restart server.
    """
    simple_update()
    with cd(env.path):
        with prefix('. PATH_TO_ENV'):
            run('pip install -r requirements.txt')
            run('python manage.py syncdb')
            run('python manage.py migrate gerenciador') # South
        
    restart_app()
