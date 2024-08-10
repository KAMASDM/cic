from celery import shared_task
from core.email_backend import dynamic_send_email
from .models import EmailTemplate
from user.models import User

@shared_task(bind=True)
def send_welcome_email(self, to:list, user_id:int):
    email_template = EmailTemplate.objects.get(name="welcome email")
    
    user_obj= User.objects.get(id = user_id)

    dynamic_send_email(subject=email_template.subject,
                       body=email_template.body,
                       to=to,
                       user=user_obj,
                       attachments=email_template.attachments
                       )
