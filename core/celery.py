from datetime import timedelta
import os
from celery.schedules import crontab

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()

app.conf.beat_scheduler = "redbeat.RedBeatScheduler"
app.conf.redbeat_redis_url = "redis://localhost:6379/3"
app.conf.beat_schedule = {
    "check-client-reminders": {
        "task": "Master.tasks.send_client_reminders",
        "schedule": 10,
    },
  
}
