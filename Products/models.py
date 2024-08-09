from django.db import models
from Master.models import Product_Category
from django.contrib.auth.models import User
from django.conf import settings
class Products(models.Model):
    Product_name = models.CharField(max_length=100)
    Product_status = models.BooleanField(default=True)
    Product_Serial_No = models.CharField(max_length=100)

    Product_category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)
    Product_image = models.ImageField(upload_to='products/')

    Product_Specification = models.TextField()
    Product_description = models.CharField(max_length=100)

    Product_Assigned_User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    Product_created_at = models.DateTimeField(auto_now_add=True)
