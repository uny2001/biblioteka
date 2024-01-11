# Generated by Django 5.0 on 2023-12-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Available"), (1, "Rented")], default=0
            ),
        ),
    ]