# Generated by Django 3.2.16 on 2023-04-16 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20230417_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ticket_description',
            new_name='event_info',
        ),
    ]