# Generated by Django 3.2.13 on 2022-05-25 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_auto_20200617_1103"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
