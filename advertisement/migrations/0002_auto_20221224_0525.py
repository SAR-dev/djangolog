# Generated by Django 3.2.16 on 2022-12-24 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='subtitle',
            field=models.CharField(blank=True, default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]
