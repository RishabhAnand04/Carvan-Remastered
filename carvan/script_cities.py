import os
import django
from django.conf import settings

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carvan.settings")

# Initialize Django.
django.setup()

from api.models import Places,Visiting
from carvan.settings import BASE_DIR
import json


def manual_post():
    with open(BASE_DIR/"carvan"/"data"/"cities.json", 'r') as file:
        data = json.load(file)
    for d in data["places"]:
        a = Places.objects.get_or_create(
            city = Places.objects.first(),
            name = d["name"],
                                rating = d["rating"],
                                visits_per_month =d["visits_per_month"],
                                ticket_price=d["ticket_price"],
                                hours_open =d["hours_open"],
                                accessibility_range=d["accessibility_range"],
                                location=d["location"],
                                description=d["description"],
                                highlight =d["highlight"],
                                family_friendly =d["family_friendly"],
                                ) 

manual_post()