# Generated by Django 4.0.4 on 2022-06-11 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QueqibApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Countries',
            new_name='City',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='Contry_name',
            new_name='City_name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='continent',
            new_name='country',
        ),
    ]