# Generated by Django 3.2.16 on 2022-12-25 05:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gig', '0017_alter_gig_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('package', '0006_auto_20221220_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(blank=True, max_length=350, null=True, validators=[django.core.validators.MinLengthValidator(15)])),
                ('due_on', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('completed', 'Completed'), ('late', 'Late'), ('cancelled', 'Cancelled')], default='pending', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_buyer', to=settings.AUTH_USER_MODEL)),
                ('gig', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_gig', to='gig.gig')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_package', to='package.package')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='order_seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
