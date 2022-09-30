"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for loading data from GRSS.
"""

# TODO: zrobić tak by ładował tylko najnowsze - te, których nie ma


from django.core.management.base import BaseCommand, CommandError

import json
from quakes.models import Quake
from django.contrib.gis.geos import Point
from datetime import datetime
from django.utils.timezone import make_aware


def load_GRSS():
    from data_fetchers.GRSS.GRSSfetcher import GRSSFetcher

    f = GRSSFetcher()
    file = f.exportData()

    geojs = json.loads(file.read_text())
    for feature in geojs["features"]:

        q = Quake(
            mag=feature["properties"]["mag"],
            date=feature["properties"]["date"],
            geom=Point(
                feature["geometry"]["coordinates"][0],
                feature["geometry"]["coordinates"][1],
            ),
            vendor='GRSS',
        )
        q.save()


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        load_GRSS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
