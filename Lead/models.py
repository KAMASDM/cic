from django.contrib.auth.models import User
from django.db import models
from Master.models import Lead_Source, Lead_Status, Industry_Type as Lead_Industry, Client_Type, lead_Followup_Status
from Products.models import Products

class Lead(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=100)
    Primary_phone = models.CharField(max_length=100)
    Mobile_phone = models.CharField(max_length=100)
    Primary_Email = models.EmailField()
    Secondary_Email = models.EmailField()
    Company_website = models.CharField(max_length=100)
    Lead_location = models.CharField(max_length=100)

    Lead_Source = models.ForeignKey(Lead_Source, on_delete=models.CASCADE)
    Lead_Status = models.ForeignKey(Lead_Status, on_delete=models.CASCADE)
    Lead_Industry = models.ForeignKey(Lead_Industry, on_delete=models.CASCADE)
    Client_Type = models.ForeignKey(Client_Type, on_delete=models.CASCADE)
    Lead_Followup_Status = models.ForeignKey(lead_Followup_Status, on_delete=models.CASCADE)
    Products = models.ManyToManyField(Products, blank=True)
    Notes = models.TextField()
    Assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
