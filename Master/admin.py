from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (
    DelayedEvent,
    EmailTemplateCategory,
    Lead_Source,
    Industry_Type,
    Lead_Status,
    Client_Type,
    lead_Followup_Status,
    Product_Category,
)


# Define resources for import/export
class LeadSourceResource(resources.ModelResource):
    class Meta:
        model = Lead_Source


class IndustryTypeResource(resources.ModelResource):
    class Meta:
        model = Industry_Type


class LeadStatusResource(resources.ModelResource):
    class Meta:
        model = Lead_Status


class ClientTypeResource(resources.ModelResource):
    class Meta:
        model = Client_Type


class LeadFollowupStatusResource(resources.ModelResource):
    class Meta:
        model = lead_Followup_Status


class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = Product_Category


# Define admin classes with search and filter capabilities
class LeadSourceAdmin(ImportExportModelAdmin):
    resource_class = LeadSourceResource
    list_display = ("source_name",)
    search_fields = ("source_name",)
    list_filter = ("source_name",)


class IndustryTypeAdmin(ImportExportModelAdmin):
    resource_class = IndustryTypeResource
    list_display = ("industry_name",)
    search_fields = ("industry_name",)
    list_filter = ("industry_name",)


class LeadStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadStatusResource
    list_display = ("status_name",)
    search_fields = ("status_name",)
    list_filter = ("status_name",)


class ClientTypeAdmin(ImportExportModelAdmin):
    resource_class = ClientTypeResource
    list_display = ("client_type_name",)
    search_fields = ("client_type_name",)
    list_filter = ("client_type_name",)


class LeadFollowupStatusAdmin(ImportExportModelAdmin):
    resource_class = LeadFollowupStatusResource
    list_display = ("followup_status_name",)
    search_fields = ("followup_status_name",)
    list_filter = ("followup_status_name",)


class ProductCategoryAdmin(ImportExportModelAdmin):
    resource_class = ProductCategoryResource
    list_display = ("category_name",)
    search_fields = ("category_name",)
    list_filter = ("category_name",)


# Register models with the admin site
admin.site.register(Lead_Source, LeadSourceAdmin)
admin.site.register(Industry_Type, IndustryTypeAdmin)
admin.site.register(Lead_Status, LeadStatusAdmin)
admin.site.register(Client_Type, ClientTypeAdmin)
admin.site.register(lead_Followup_Status, LeadFollowupStatusAdmin)
admin.site.register(Product_Category, ProductCategoryAdmin)


@admin.register(EmailTemplateCategory)
class EmailTemplateCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DelayedEvent)
class DelayedEventAdmin(admin.ModelAdmin):
    list_display = (
        "event_type",
        "due_date",
        "is_processed",
    )
    
    list_filter = ('is_processed',)