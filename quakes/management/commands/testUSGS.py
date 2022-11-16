"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for TESTING loading data from USGS.
"""

from django.core.management.base import BaseCommand, CommandError
import data_fetchers.USGS.USGSQuakesCounter as uqc
import data_fetchers.USGS.USGSFetcher as uf
import data_fetchers.USGS.USGSQuakesExporter as uqe



def test_count_quakes():
    uqc.count_quakes('2010-03-01', '2010-06-30')
    #uqc.count_quakes('2021-01-01', '2021-04-01')

def test_QueryMode():
    f = uf.USGSFetcher(mode='fdsnws', starttime='2021-01-01', endtime='2021-02-01')
    f.exportData()

def test_quakes_exporter():
    uqe.export_quakes('2010-03-01', '2010-06-30')
    #uqe.export_quakes('2021-01-01', '2021-04-01')


    


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        #test_count_quakes()
        #test_QueryMode()
        test_quakes_exporter()
        self.stdout.write(self.style.SUCCESS("TESTS COMPLETED!"))
