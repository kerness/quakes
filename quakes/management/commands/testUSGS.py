"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for TESTING loading data from USGS.
"""

from django.core.management.base import BaseCommand, CommandError

import json
from quakes.models import Quake
from django.contrib.gis.geos import Point
from datetime import datetime
from django.utils.timezone import make_aware
# from data_fetchers.USGS.USGSFetcher import USGSFetcher
import data_fetchers.USGS.USGSQuakesCounter as t
import data_fetchers.USGS.USGSFetcher as uf
import sys


# TODO: naprawić daty tak żeby tylko data była bez godziny
def test_USGS():
    print(sys.path)
    #f = USGSFetcher(level="1.0", period="day")
    t.count_quakes('2010-03-01', '2010-06-30')

def test_QueryMode():
    fetcher = uf.USGSFetcher(mode='fdsnws', starttime='2021-01-01', endtime='2021-05-01', count=True)
    fetcher.fetch_data_fdsnws()
    


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        #test_USGS()
        test_QueryMode()
        self.stdout.write(self.style.SUCCESS("TESTS COMPLETED!"))
