from django.contrib import admin

from .models import EmailTemplate, EmailAttachment

class EmailAttachmentInline(admin.TabularInline):
    model = EmailAttachment
    fk_name = 'email_template'
    extra =1 
@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email_category',
        'product',
        'subject',
        'body',
        'created_by',
        'created_at',
        'updated_at',
        'trigger',
    )
    list_filter = (
        'email_category',
        'product',
        'created_by',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    
    inlines = [EmailAttachmentInline]
