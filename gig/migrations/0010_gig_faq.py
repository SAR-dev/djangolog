# Generated by Django 3.2.16 on 2022-12-17 01:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0009_auto_20221212_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='faq',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=500), default=list, size=8),
        ),
    ]
