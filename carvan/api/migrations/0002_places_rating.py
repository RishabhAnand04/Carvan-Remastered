# Generated by Django 4.2.5 on 2023-09-18 08:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="places",
            name="rating",
            field=models.IntegerField(null=True),
        ),
    ]