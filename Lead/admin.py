from typing import Any
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
    list_display = (
        "first_name",
        "last_name",
        "company_name",
        "primary_phone",
        "primary_email",
        "lead_source",
        "lead_status",
        "lead_Industry",
        "client_type",
        "created_at",
    )
    search_fields = (
        "first_name",
        "last_name",
        "company_name",
        "primary_phone",
        "primary_email",
    )
    list_filter = (
        "lead_source",
        "lead_status",
        "lead_Industry",
        "client_type",
        "created_at",
    )
    filter_horizontal = ("products",)
    ordering = ("-created_at",)

    fieldsets = (
        ("Personal Information", {"fields": ("first_name", "last_name")}),
        ("Company Information", {"fields": ("company_name", "company_website")}),
        (
            "Contact Information",
            {
                "fields": (
                    "primary_phone",
                    "mobile_phone",
                    "primary_email",
                    "secondary_email",
                )
            },
        ),
        (
            "Lead Details",
            {
                "fields": (
                    "lead_location",
                    "lead_source",
                    "lead_status",
                    "lead_Industry",
                    "client_type",
                    "lead_followup_status",
                    "assigned_to",
                    "products",
                    "notes",
                )
            },
        ),
    )

    readonly_fields = ("created_at",)

    def save_model(self, request: Any, obj: Any, form: Any, change: bool) -> None:
        if not change:
            obj.created_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Lead, LeadAdmin)
