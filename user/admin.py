from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(UserAdmin):

    extra_fieldsets = (
        (
            "Email",
            {
                "fields": (
                    "email_host",
                    "email_port",
                    "email_username",
                    "email_password",
                    "email_use_tls",
                    "from_email",
                ),
            },
        ),
    )
    
    fieldsets = UserAdmin.fieldsets+ extra_fieldsets