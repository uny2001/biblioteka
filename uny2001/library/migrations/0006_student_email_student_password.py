# Generated by Django 5.0 on 2023-12-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0005_book_age_restriction"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.CharField(
                db_index=True, default="email@example.com", max_length=200
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="password",
            field=models.CharField(default="password", max_length=200),
            preserve_default=False,
        ),
    ]
