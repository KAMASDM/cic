from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Products

# Define the resource for import/export
class ProductsResource(resources.ModelResource):
    class Meta:
        model = Products

# Define the admin class with search, filter, and fieldsets capabilities
class ProductsAdmin(ImportExportModelAdmin):
    resource_class = ProductsResource
    list_display = ('Product_name', 'Product_status', 'Product_Serial_No', 'Product_category', 'Product_Assigned_User', 'Product_created_at')
    search_fields = ('Product_name', 'Product_Serial_No', 'Product_description')
    list_filter = ('Product_status', 'Product_category', 'Product_Assigned_User', 'Product_created_at')
    list_display_links = ('Product_name', 'Product_Serial_No')
    ordering = ('-Product_created_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('Product_name', 'Product_status', 'Product_Serial_No', 'Product_category', 'Product_image')
        }),
        ('Details', {
            'fields': ('Product_Specification', 'Product_description', 'Product_Assigned_User')
        }),
    )

    readonly_fields = ('Product_created_at',)

# Register the model with the admin site
admin.site.register(Products, ProductsAdmin)
