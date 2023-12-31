# Generated by Django 3.2.11 on 2023-09-28 08:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("app_sin_bau_api", "0006_alter_tb_1_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tb_1",
            options={"ordering": ["_time"], "verbose_name": "用戶資料庫", "verbose_name_plural": "用戶資料庫"},
        ),
        migrations.AddField(
            model_name="tb_1",
            name="_time",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
