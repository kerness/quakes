"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for exporting data from USGS from 20 years.
"""

from django.core.management.base import BaseCommand

import data_fetchers.USGS.USGSQuakesExporter as uqe
import data_fetchers.USGS.utils.dbLoad as dl

def export_USGS():
    from data_fetchers.USGS.USGSFetcher import USGSFetcher
    #exports = uqe.export_quakes('2010-03-01', '2010-06-30')
    exports = uqe.export_quakes('2021-06-01', '2021-07-01')
    print("Ponrano: ", len(exports), " zestawów danych. Następuje ładowanie do bazy danych...")
    for export in exports:
        print(export)
        dl.load_to_django_db(export)

class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        export_USGS()
        self.stdout.write(self.style.SUCCESS("Data Loaded to Database"))
