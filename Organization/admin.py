from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Organization

User = get_user_model()

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('organization_name', 'primary_phone', 'primary_email', 'industry', 'assigned_to')
    list_filter = ('industry', 'assigned_to')
    search_fields = ('organization_name', 'primary_email', 'website')
    readonly_fields = ('id',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('organization_name', 'industry', 'assigned_to')
        }),
        ('Contact Information', {
            'fields': ('primary_phone', 'primary_email', 'website')
        }),
        ('Address Information', {
            'fields': ('organization_location', 'postal_address'),
        }),
        ('Additional Information', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(assigned_to=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "assigned_to":
            kwargs["queryset"] = User.objects.filter(is_staff=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.assigned_to = request.user
        super().save_model(request, obj, form, change)