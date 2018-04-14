# Generated by Django 2.0.2 on 2018-04-09 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friendsbook', '0002_profile_profileviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='createdBy',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createdBy', to=settings.AUTH_USER_MODEL),
        ),
    ]
