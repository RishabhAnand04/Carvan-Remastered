# Generated by Django 4.2.5 on 2023-09-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_visiting_image_str"),
    ]

    operations = [
        migrations.AddField(
            model_name="places",
            name="sub_heading",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="places",
            name="name",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
