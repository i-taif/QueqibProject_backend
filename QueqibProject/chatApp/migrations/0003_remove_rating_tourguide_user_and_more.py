# Generated by Django 4.0.4 on 2022-06-14 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatApp', '0002_rating_tourguide_user_alter_rating_client_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='TourGuide_user',
        ),
        migrations.AlterField(
            model_name='rating',
            name='client_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
