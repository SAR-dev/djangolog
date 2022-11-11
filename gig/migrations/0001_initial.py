# Generated by Django 3.2.16 on 2022-11-11 03:13

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '0001_initial'),
        ('tag', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', models.TextField()),
                ('languages', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), size=8)),
                ('expertises', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), size=8)),
                ('specializations', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=8), size=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='gig_category', to='category.category')),
                ('downvotes', models.ManyToManyField(related_name='gig_downvotes', to=settings.AUTH_USER_MODEL)),
                ('images', models.ManyToManyField(related_name='gig_images', to='image.Image')),
                ('tags', models.ManyToManyField(blank=True, default=None, related_name='gig_tags', to='tag.Tag')),
                ('upvotes', models.ManyToManyField(related_name='gig_upvotes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
