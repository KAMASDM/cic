from django.db import models

# Create your models here.
class Lead_Source(models.Model):
    source_name = models.CharField(max_length=100)

    def __str__(self):
        return self.source_name

class Industry_Type(models.Model):
    industry_name = models.CharField(max_length=100)

    def __str__(self):
        return self.industry_name

class Lead_Status(models.Model):
    status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.status_name

class Client_Type(models.Model):
    client_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.client_type_name

class lead_Followup_Status(models.Model):
    followup_status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.followup_status_name

class Product_Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class EmailTemplateCategory(models.Model):
    category = models.CharField(max_length=50)

