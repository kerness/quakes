"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for loading data from USGS.
"""

from django.core.management.base import BaseCommand, CommandError

import json
from quakes.models import Quake
from django.contrib.gis.geos import Point
from datetime import datetime
from django.utils.timezone import make_aware

# TODO: naprawić daty tak żeby tylko data była bez godziny
def load_USGS():
    from data_fetchers.USGS.USGSFetcher import USGSFetcher

    f = USGSFetcher("feed", "significant", "day")
    file = f.exportData()

    geojs = json.loads(file.read_text())
    for feature in geojs["features"]:

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


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        load_USGS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
