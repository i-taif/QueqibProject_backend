# Generated by Django 4.0.4 on 2022-06-13 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QueqibApp', '0006_profile_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='city',
            new_name='cities',
        ),
        migrations.RemoveField(
            model_name='post',
            name='city',
        ),
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.URLField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='cities',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='QueqibApp.city'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.URLField(max_length=300),
        ),
    ]