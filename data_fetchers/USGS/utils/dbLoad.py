import json
from quakes.models import Quake
from django.contrib.gis.geos import Point
from datetime import datetime
from django.utils.timezone import make_aware
from django.db import IntegrityError


def load_to_django_db(file):
    geojs = json.loads(file.read_text())
    for feature in geojs["features"]:

        # jeśli nie ma wartości magnitudy - pomiń
        if feature["properties"]["mag"] is None:
            continue

        q = Quake(
            mag=feature["properties"]["mag"],
            date=make_aware(datetime.fromtimestamp(feature["properties"]["time"]/1000)).date(), # EDITED: get only date!
            # może wcześniej zamienic na to takie datetime
            #date="2022-01-17 18:50:52",
            geom=Point(
                feature["geometry"]["coordinates"][0],
                feature["geometry"]["coordinates"][1],
            ),
            vendor='USGS',
        )

        q.save()
