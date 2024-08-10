from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from Master.models import EmailTemplateCategory
class EmailTemplate(models.Model):
    name = models.CharField(max_length=100)
    email_category = models.ForeignKey(EmailTemplateCategory, on_delete=models.CASCADE)
    product = models.ForeignKey('Products.Products', on_delete=models.CASCADE, blank=True, null=True)
    subject = models.CharField(max_length=200)
    body = RichTextField() 
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    TRIGGER_CHOICES = [
        ('NEW_LEAD' , 'New Lead') ,
        ('LEAD_STATUS_CHANGE' , 'Lead Status Change') ,
        ('NEW_ORGANIZATION' , 'New Organization') ,
        ('NEW_PRODUCT' , 'New Product') ,
        # Add more trigger types as needed
    ]
    trigger = models.CharField(max_length=50 , choices=TRIGGER_CHOICES)

    def _str_(self):
        return self.name
        
class EmailAttachment(models.Model):
    file = models.FileField(upload_to= "emails/attachments")
    name = models.CharField( max_length=50)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE, related_name='attachments')
    
    def __str__(self):
        return f"{self.name}"