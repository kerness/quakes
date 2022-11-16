import data_fetchers.USGS.dateRangeOperations as dro
from datetime import datetime
from datetime import timedelta
import requests


def downloadData(start, end):
    url = f"https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&starttime={start}&endtime={end}"
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise IOError(e)

    return list(r.json().values())[0]


def over_limit_ranges_count(over_limit_ranges):
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

    # pętla do wykonania zapytań w trzech okresach któ©e na siebie nie nachodzą
    for mdr in month_4_add1:
        #print(mdr)
        res = downloadData(mdr[0], mdr[1])
        print("Zakres dat: ", mdr[0], mdr[1], "Count:", res)
        res = downloadData(mdr[2], mdr[3])
        print("Zakres dat: ", mdr[2], mdr[3], "Count:", res)
        res = downloadData(mdr[4], mdr[5])
        print("Zakres dat: ", mdr[4], mdr[5], "Count:", res)


def count_quakes(start, end):
    over_limit_ranges = []
    month_ranges = dro.prepare_month_ranges(start, end)
    for range in month_ranges:
        res = downloadData(range[0], range[1])
        print("Zakres dat: ", range, "Count:", res)
        if res > 20000:
            over_limit_ranges.append(range)
            print("\tOver 20000. Spliting into smaller intervals.")
            over_limit_ranges_count([range])

    

