# Generated by Django 3.2.6 on 2022-10-10 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tag', '0001_initial'),
        ('category', '0001_initial'),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='category.category')),
                ('cover', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cover', to='image.image')),
                ('images', models.ManyToManyField(blank=True, default=None, related_name='images', to='image.Image')),
                ('tags', models.ManyToManyField(blank=True, default=None, related_name='tags', to='tag.Tag')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
