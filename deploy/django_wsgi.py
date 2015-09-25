import os, sys

#Python/Django location
sys.path.insert(0, '/home/olga/mysite/django_env/')
sys.path.insert(0, '/home/olga/mysite/django_env/lib/python2.7/site-packages')

#Project location
sys.path.insert(0,'/home/olga/mysite/django_env/mysite/')
sys.path.insert(0,'/home/olga/mysite/')

#Project config file
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
