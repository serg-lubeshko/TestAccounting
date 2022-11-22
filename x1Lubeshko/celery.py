import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'x1Lubeshko.settings')

app = Celery('x1Lubeshko')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'add-day': {
#         'task': 'send_notification',
#         'schedule': crontab(minute=0, hour=8, day_of_week='mon-sun'),
#     }
# }
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'x1Lubeshko.tasks.send_notification',
        'schedule': crontab()
    }
}
