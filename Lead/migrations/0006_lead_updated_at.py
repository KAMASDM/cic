# Generated by Django 5.0.7 on 2024-08-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lead', '0005_alter_lead_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
