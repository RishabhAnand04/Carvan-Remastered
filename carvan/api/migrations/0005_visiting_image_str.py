# Generated by Django 4.2.5 on 2023-09-18 19:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_places_imgage_visiting_imgage"),
    ]

    operations = [
        migrations.AddField(
            model_name="visiting",
            name="image_str",
            field=models.CharField(default="", max_length=200),
        ),
    ]