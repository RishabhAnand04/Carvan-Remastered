# Generated by Django 4.2.5 on 2023-09-19 00:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_alter_visiting_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="visiting",
            name="details",
            field=models.CharField(default="", max_length=500),
        ),
        migrations.AddField(
            model_name="visiting",
            name="i_frame",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AddField(
            model_name="visiting",
            name="sub_heading",
            field=models.CharField(default="", max_length=200),
        ),
    ]