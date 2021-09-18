import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
# Make sure to add all different queues here for a worker to listen to all the queues automatically
# More info https://docs.celeryproject.org/en/stable/userguide/routing.html#defining-queues
app.conf.task_queues = (
    Queue('celery'),
    Queue('sms'),
)


@app.task(bind=True)
def debug_task(self):
    """Boilerplate debug task which checks celery setup."""
    print(f'Request: {self.request!r}')
