# Generated by Django 4.2.5 on 2023-09-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_places_sub_heading_alter_places_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visiting",
            name="rating",
            field=models.FloatField(null=True),
        ),
    ]
