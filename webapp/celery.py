from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')

app = Celery('webapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
