import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mlog_project.settings')
app = Celery('mlog_projects')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()