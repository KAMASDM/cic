from django.apps import AppConfig


class LeadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Lead'
    def ready(self) -> None:
        from . import receiver