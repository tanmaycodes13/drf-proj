# Generated by Django 3.1.8 on 2023-10-17 18:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tv_series", "0002_netflix_seires_test"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="netflix_seires",
            name="test",
        ),
    ]
