import data_fetchers.USGS.USGSFetcher as uf
import data_fetchers.USGS.utils.USGSQuakesCounter as uqc
import data_fetchers.USGS.utils.dateRangeOperations as dro
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import requests

def handle_over_limit_ranges(over_limit_ranges):
    """Funkcja do obsługi miesięcy w którch liczba obserwacji przekracza 20000"""
    # over_limit_ranges = [('2010-04-01', '2010-04-30'), ('2018-06-01', '2018-06-30'), ('2018-07-01', '2018-07-31'), ('2019-07-01', '2019-07-31'), ('2020-06-01', '2020-06-30')]
    # dzieli podane miesiące na trzy okresy i zamienia je na obiekty datetime
    month_4 = [
        list(
            map(
                lambda x: datetime.strptime(x, "%Y-%m-%d"),
                list(dro.split_date_range(r[0], r[1], 3)),
            )
        )
        for r in over_limit_ranges
    ]
    month_4_add1 = []
    # dodaje dwie daty do każdego miesiąca tak aby możliwe było wykonanie zapytania bez nachodzących na siebie dat
    for date_range in month_4:
        date_range.insert(2, (date_range[1] + timedelta(days=1)))
        date_range.insert(4, (date_range[3] + timedelta(days=1)))
    # zamienia datetime na string - ta lista jest gotowa do wykonania zapytań
    month_4_add1 = [[d.strftime("%Y-%m-%d") for d in group] for group in month_4]
    exported_files = []
    # pętla do wykonania zapytań w trzech okresach któ©e na siebie nie nachodzą
    for mdr in month_4_add1:
        #print(mdr)
        f = uf.USGSFetcher(mode="fdsnws", starttime=mdr[0], endtime=mdr[1])
        res = f.exportData()
        exported_files.append(res)
        f = uf.USGSFetcher(mode="fdsnws", starttime=mdr[2], endtime=mdr[3])
        res = f.exportData()
        exported_files.append(res)
        f = uf.USGSFetcher(mode="fdsnws", starttime=mdr[4], endtime=mdr[5])
        res = f.exportData()
        exported_files.append(res)
    
    return exported_files


def export_quakes(start, end):
    over_limit_ranges = []
    exported_files = []
    month_ranges = dro.prepare_month_ranges(start, end)
    for range in month_ranges:
        count = uqc.downloadData(range[0], range[1])
        print("Zakres dat: ", range, "Count:", count)
        if count < 20000:
            f = uf.USGSFetcher(mode="fdsnws", starttime=range[0], endtime=range[1])
            res = f.exportData()
            exported_files.append(res)
        if count > 20000:
            over_limit_ranges.append(range)
            print("\tOver 20000. Spliting into smaller intervals.")
            res = handle_over_limit_ranges([range])
            exported_files = exported_files + res
    return exported_files


    

