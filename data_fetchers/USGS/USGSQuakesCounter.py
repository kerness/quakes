from .USGSFetcher import USGSFetcher
from datetime import datetime
from datetime import timedelta
import numpy as np
import datetime as dt

import dateRangeOperations as dro


# def dateRange(start="2000-01-01", end="2000-12-31"):
#     # https://stackoverflow.com/questions/63637444/python-month-start-and-end-dates-between-two-dates
#     start_date = np.datetime64(start[:-3])
#     # Add one month to end date so last month is included
#     end_date = np.datetime64(end[:-3]) + np.timedelta64(1, "M")
#     # Create Date Range
#     date_range = np.arange(start_date, end_date, dtype="datetime64[M]")
#     # Add 5 AM to start_dates
#     start_dates = date_range + np.timedelta64(5, "h")
#     # Add 1 Month and subrtract 4 hours to 8 PM on last day of month
#     end_dates = date_range + np.timedelta64(1, "M") - np.timedelta64(4, "h")
#     # Apply Formatting
#     final_start_dates = [
#         parse_date(np.datetime_as_string(d, unit="s")) for d in start_dates
#     ]
#     final_end_dates = [
#         parse_date(np.datetime_as_string(d, unit="s")) for d in end_dates
#     ]

#     return final_start_dates, final_end_dates


# def parse_date(date_string):
#     # parse numpy date string
#     date_time = date_string.split("T")
#     date_parts = date_time[0].split("-")
#     time_parts = date_time[1][:-1].split(":")
#     # convert string values to ints
#     datetime_ints = [int(d) for d in date_parts] + [int(time_parts[0])]

#     # apply formatting
#     return dt.datetime(*datetime_ints).strftime("%Y-%m-%d")


# def prepare_month_ranges(start, end):
#     start, end = dateRange(start, end)
#     month_ranges = []
#     for s, e in zip(start, end):
#         month_ranges.append((s, e))
#     return month_ranges


def count_quakes(start, end):
    over_limit_ranges = []
    month_ranges = dro.prepare_month_ranges(start, end)
    for range in month_ranges:
        fetcher = USGSFetcher(
            "fdsnws", starttime=range[0], endtime=range[1], count=True
        )
        res = fetcher.exportData()
        print("Zakres dat: ", range, "Count:", res)
        if res > 20000:
            over_limit_ranges.append(range)
            print("!!!!!!!!!!!!!!!!!!!ZA DUŻO!!!!!!!!!!!!!!!!!!!!!")

    over_limit_ranges_count(over_limit_ranges)


# def split_date_range(start, end, intv):
#     """Divide a date range into intervals"""
#     from datetime import datetime

#     start = datetime.strptime(start, "%Y-%m-%d")
#     end = datetime.strptime(end, "%Y-%m-%d")
#     diff = (end - start) / intv
#     for i in range(intv):
#         yield (start + diff * i).strftime("%Y-%m-%d")
#     yield end.strftime("%Y-%m-%d")


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
        print(mdr)
        fetcher = USGSFetcher("fdsnws", starttime=mdr[0], endtime=mdr[1], count=True)
        res = fetcher.exportData()
        print("Zakres dat: ", mdr[0], mdr[1], "Count:", res)
        fetcher = USGSFetcher("fdsnws", starttime=mdr[2], endtime=mdr[3], count=True)
        res = fetcher.exportData()
        print("Zakres dat: ", mdr[2], mdr[3], "Count:", res)
        fetcher = USGSFetcher("fdsnws", starttime=mdr[4], endtime=mdr[5], count=True)
        res = fetcher.exportData()
        print("Zakres dat: ", mdr[4], mdr[5], "Count:", res)