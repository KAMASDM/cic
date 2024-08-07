from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Lead

# Define the resource for import/export
class LeadResource(resources.ModelResource):
    class Meta:
        model = Lead

# Define the admin class with search, filter, and fieldsets capabilities
class LeadAdmin(ImportExportModelAdmin):
    resource_class = LeadResource
    list_display = ('First_name', 'Last_name', 'Company_name', 'Primary_phone', 'Primary_Email', 'Lead_Source', 'Lead_Status', 'Lead_Industry', 'Client_Type', 'created_at')
    search_fields = ('First_name', 'Last_name', 'Company_name', 'Primary_phone', 'Primary_Email')
    list_filter = ('Lead_Source', 'Lead_Status', 'Lead_Industry', 'Client_Type', 'created_at')
    filter_horizontal = ('Products',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Personal Information', {
            'fields': ('First_name', 'Last_name')
        }),
        ('Company Information', {
            'fields': ('Company_name', 'Company_website')
        }),
        ('Contact Information', {
            'fields': ('Primary_phone', 'Mobile_phone', 'Primary_Email', 'Secondary_Email')
        }),
        ('Lead Details', {
            'fields': ('Lead_location', 'Lead_Source', 'Lead_Status', 'Lead_Industry', 'Client_Type', 'Lead_Followup_Status','Assigned_to', 'Products', 'Notes')
        }),
    )

    readonly_fields = ('created_at',)

# Register the model with the admin site
admin.site.register(Lead, LeadAdmin)
