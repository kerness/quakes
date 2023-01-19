"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for loading data from USGS.
"""

from django.core.management.base import BaseCommand

import data_fetchers.USGS.utils.dbLoad as dl


def load_USGS():
    from data_fetchers.USGS.USGSFetcher import USGSFetcher

    f = USGSFetcher(mode="feed", level="all", period="month")
    file = f.exportData()
    dl.load_to_django_db(file)


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        load_USGS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
