from email_templates.tasks import send_welcome_email
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead

@receiver(post_save, sender=Lead)
def post_save_receiver(sender, created, instance:Lead, **kwargs):
    if created:
        instance.assigned_to = instance.created_by
        instance.save() 
        send_welcome_email.delay(
            to=[instance.primary_email, instance.secondary_email],
            user_id=instance.assigned_to.id,
        )
