# Generated by Django 4.0.4 on 2022-06-11 15:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QueqibApp', '0003_rename_country_post_city_rename_country_profile_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
