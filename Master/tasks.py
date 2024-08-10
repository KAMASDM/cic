from celery import shared_task
from Master.models import DelayedEvent
from django.utils import timezone
from core.email_backend import dynamic_send_email


@shared_task(bind=True)
def send_client_reminders(self):
    print(timezone.now())
    events = DelayedEvent.objects.filter(
        due_date__lte=timezone.now(), event_type="client_reminder", is_processed=False
    )
    if events.count() != 0:
        for event in events:

            if dynamic_send_email(
                **event.data.get("email_data", {}), config=event.data.get("config", {})
            ):

                event.is_processed = True
                event.save(update_fields=["is_processed"])
