# Generated by Django 3.2.16 on 2022-12-05 01:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
        ('gig', '0002_auto_20221128_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='expertises',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=8),
        ),
        migrations.AlterField(
            model_name='gig',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, related_name='gig_images', to='image.Image'),
        ),
        migrations.AlterField(
            model_name='gig',
            name='languages',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=8),
        ),
        migrations.AlterField(
            model_name='gig',
            name='specializations',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, size=8),
        ),
    ]