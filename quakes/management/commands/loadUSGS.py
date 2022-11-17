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

import data_fetchers.USGS.utils.dbLoad as dl

# TODO: naprawić daty tak żeby tylko data była bez godziny
def load_USGS():
    from data_fetchers.USGS.USGSFetcher import USGSFetcher

    f = USGSFetcher(mode="feed", level="1.0", period="day")
    file = f.exportData()
    dl.load_to_django_db(file)

class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        load_USGS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
