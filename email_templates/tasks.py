from celery import shared_task
from core.email_backend import dynamic_send_email
from .models import EmailTemplate
from user.models import User
from Lead.models import Lead

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
                       
@shared_task(bind=True)
def send_product_questionaire_email(self, lead_id:int):
    """This sends emails of all the products that are in a lead.

    Args:
        to (list): list of emails that will receive the email
        user_id (int): id of the Lead Id.
    """
    
    lead= Lead.objects.get(id=lead_id)
    assiged_user = lead.assigned_to
    _to = [lead.primary_email, lead.secondary_email]
    to = [i for i in _to if i]
    email_templates = EmailTemplate.objects.filter(product__in=lead.products.all())
    
    for email_template in email_templates:
        dynamic_send_email(subject=email_template.subject,
                        body=email_template.body,
                        to=to,
                        user=assiged_user,
                        attachments=email_template.attachments
                        )
    
    # user_obj= User.objects.get(id = user_id)
    
    
def create_reminders_for_questionaire_reply(self):...