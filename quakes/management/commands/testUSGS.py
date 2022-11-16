"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for TESTING loading data from USGS.
"""

from django.core.management.base import BaseCommand, CommandError
import data_fetchers.USGS.USGSQuakesCounter as uqc
import data_fetchers.USGS.USGSFetcher as uf



def test_count_quakes():
    uqc.count_quakes('2010-03-01', '2010-06-30')
    #uqc.count_quakes('2021-01-01', '2021-04-01')

def test_QueryMode():
    fetcher = uf.USGSFetcher(mode='fdsnws', starttime='2021-01-01', endtime='2021-05-01', count=True)
    fetcher.count_quakes()

    


class Command(BaseCommand):
    help = "Loads data from USGS"

    def handle(self, *args, **options):
        test_count_quakes()
        #test_QueryMode()
        self.stdout.write(self.style.SUCCESS("TESTS COMPLETED!"))
