# Generated by Django 3.2.11 on 2023-12-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_sin_bau_api", "0010_auto_20231206_0904"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="created_by",
            field=models.TextField(blank=True, verbose_name="created_by"),
        ),
    ]
