# Generated by Django 3.2.16 on 2022-12-18 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0004_auto_20221218_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='extra_services',
        ),
    ]
