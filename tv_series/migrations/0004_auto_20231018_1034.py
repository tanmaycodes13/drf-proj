# Generated by Django 3.1.8 on 2023-10-18 10:34

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tv_series', '0003_remove_netflix_seires_test'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='netflix_seires',
            new_name='netflix_seires_model',
        ),
    ]
