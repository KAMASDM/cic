from django.db import models
from Master.models import (
    Lead_Source,
    Lead_Status,
    Industry_Type as Lead_Industry,
    Client_Type,
    lead_Followup_Status,
)
from Products.models import Products
from django.conf import settings


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=100)
    mobile_phone = models.CharField(max_length=100)
    primary_email = models.EmailField()
    secondary_email = models.EmailField()
    company_website = models.CharField(max_length=100)
    lead_location = models.CharField(max_length=100)

    lead_source = models.ForeignKey(Lead_Source, on_delete=models.CASCADE)
    lead_status = models.ForeignKey(Lead_Status, on_delete=models.CASCADE)
    lead_Industry = models.ForeignKey(Lead_Industry, on_delete=models.CASCADE)
    client_type = models.ForeignKey(Client_Type, on_delete=models.CASCADE)
    lead_followup_status = models.ForeignKey(
        lead_Followup_Status, on_delete=models.CASCADE
    )
    products = models.ManyToManyField(Products, blank=True)
    notes = models.TextField()
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="+",null=True, blank=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# @receiver(post_save, sender=Lead)
# def send_email_on_lead_status_change(sender, created, instance:Lead, **kwargs):
#     if instance.lead_status == 'Welcome Email Sent':
#         pass
        
#     instance.save() 
#     send_welcome_email.delay(
#         to=[instance.primary_email, instance.secondary_email],
#         user_id=instance.created_by.id,
#     )
