"""
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/

A cutom managment script for TESTING loading data from USGS.
"""

from django.core.management.base import BaseCommand
import data_fetchers.USGS.utils.USGSQuakesCounter as uqc
import data_fetchers.USGS.USGSFetcher as uf
import data_fetchers.USGS.USGSQuakesExporter as uqe


def test_count_quakes():
    uqc.count_quakes("2010-03-01", "2010-06-30")
    # uqc.count_quakes('2021-01-01', '2021-04-01')


def test_QueryMode():
    f = uf.USGSFetcher(mode="fdsnws", starttime="2021-01-01", endtime="2021-02-01")
    f.exportData()


def test_quakes_exporter(start, end):
    uqe.export_quakes(start, end)
    # uqe.export_quakes('2021-01-01', '2021-04-01')


class Command(BaseCommand):
    help = "Loads data from USGS"

    def add_arguments(self, parser):
        parser.add_argument("--start", type=str, required=True)
        parser.add_argument("--end", type=str, required=True)

    def handle(self, *args, **options):
        # test_count_quakes()
        # test_QueryMode()
        # test_quakes_exporter()
        print(options["start"], options["end"])
        test_quakes_exporter(options["start"], options["end"])
        self.stdout.write(self.style.SUCCESS("TESTS COMPLETED!"))
