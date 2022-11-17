import json
from quakes.models import Quake
from django.contrib.gis.geos import Point
from django.db import IntegrityError


# def get_list_of_ids():
#     ids = Quake.objects.all()


def load_to_django_db(file):
    geojs = json.loads(file.read_text())
    for feature in geojs["features"]:

        q = Quake(
            source_system_id=feature["properties"]["unique_id"],
            mag=feature["properties"]["mag"],
            date=feature["properties"]["date"],
            geom=Point(
                feature["geometry"]["coordinates"][0],
                feature["geometry"]["coordinates"][1],
            ),
            vendor="GRSS",
        )
        try:
            q.save()
        except IntegrityError as e:
            print(e)
            continue
