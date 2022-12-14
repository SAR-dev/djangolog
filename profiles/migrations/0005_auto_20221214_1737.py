# Generated by Django 3.2.16 on 2022-12-14 08:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20221128_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='tagline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='certifications',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=8),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='educations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=8),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), default=list, size=8),
        ),
    ]
