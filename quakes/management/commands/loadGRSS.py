"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for loading data from GRSS.
"""


from django.core.management.base import BaseCommand
import data_fetchers.GRSS.utils.dbLoad as dl


def load_GRSS():
    from data_fetchers.GRSS.GRSSfetcher import GRSSFetcher

    f = GRSSFetcher()
    file = f.exportData()
    dl.load_to_django_db(file)


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        load_GRSS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
