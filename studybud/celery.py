# studybud/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studybud.settings')

app = Celery('studybud')

# Configure Celery to use settings from Django settings file
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks in all registered Django apps
app.autodiscover_tasks()

# This ensures tasks are always available to Celery

