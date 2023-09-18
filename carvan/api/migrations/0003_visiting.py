# Generated by Django 4.2.5 on 2023-09-18 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_places_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visiting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("rating", models.IntegerField(null=True)),
                ("visits_per_month", models.IntegerField(null=True)),
                ("ticket_price", models.IntegerField(null=True)),
                ("hours_open", models.IntegerField(null=True)),
                ("accessibility_range", models.IntegerField(null=True)),
                ("location", models.CharField(max_length=200)),
                ("highlight", models.CharField(max_length=200)),
                ("family_friendly", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=200)),
                (
                    "city",
                    models.ForeignKey(
                        max_length=200,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.places",
                    ),
                ),
            ],
        ),
    ]
