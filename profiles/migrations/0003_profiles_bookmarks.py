# Generated by Django 3.2.16 on 2022-11-14 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gig', '0001_initial'),
        ('profiles', '0002_auto_20221111_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarks', to='gig.Gig'),
        ),
    ]