from datetime import timedelta
from typing import Any
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from user.models import User
from .models import Lead
from email_templates.tasks import send_product_questionaire_email
from Master.models import DelayedEvent
from django.utils import timezone


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
        (
            "Meta Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                    "created_by",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
        "created_by",
    )

    def save_model(self, request: Any, obj: Lead, form: Any, change: bool) -> None:
        if not change:
            obj.created_by = request.user

        if change:
            changed_fields = form.changed_data
            if (
                "lead_status" in changed_fields
                and form.cleaned_data.get("lead_status").status_name
                == "Welcome Email Received"
            ):
                send_product_questionaire_email.delay(lead_id=obj.id)

                user: User = obj.assigned_to

                for i in [2, 4, 8, 12]:

                    DelayedEvent.objects.create(
                        event_type="client_reminder",
                        due_date=timezone.now() + timedelta(minutes=i),
                        data={
                            "email_data": {
                                "from": user.from_email,
                                "subject": "Reminder!",
                                "body": "This is a reminder for your reply.",
                                "to": [obj.primary_email, obj.secondary_email],
                            },
                            "config": {
                                "password": user.email_password,
                                "Username": user.email_username,
                                "port": user.email_port,
                                "host": user.email_host,
                            },
                        },
                    )

        return super().save_model(request, obj, form, change)


admin.site.register(Lead, LeadAdmin)
