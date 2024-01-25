# Generated by Django 5.0.1 on 2024-01-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weather',
            old_name='apparent_temperature',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='weather',
            old_name='cloud_cover',
            new_name='longitude',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='city',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='date',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='description',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='precipitation',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='rain',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='snowfall',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='wind_direction',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='wind_speed',
        ),
    ]