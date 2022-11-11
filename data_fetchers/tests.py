import USGS.USGSFetcher as uf
import pandas as pd
from datetime import datetime
from datetime import timedelta

import numpy as np
import datetime as dt

def dateRange(start='2000-01-01', end='2000-12-31'):
    # https://stackoverflow.com/questions/63637444/python-month-start-and-end-dates-between-two-dates
    start_date = np.datetime64(start[:-3])  
    #Add one month to end date so last month is included
    end_date = np.datetime64(end[:-3]) + np.timedelta64(1, 'M')
    #Create Date Range
    date_range = np.arange(start_date, end_date, dtype='datetime64[M]')
    #Add 5 AM to start_dates
    start_dates = date_range + np.timedelta64(5, 'h')
    #Add 1 Month and subrtract 4 hours to 8 PM on last day of month
    end_dates = date_range + np.timedelta64(1, 'M') - np.timedelta64(4, 'h')
    #Apply Formatting   
    final_start_dates = [parse_date(np.datetime_as_string(d, unit='s')) for d in start_dates]
    final_end_dates = [parse_date(np.datetime_as_string(d, unit='s')) for d in end_dates]
    
    return final_start_dates, final_end_dates

def parse_date(date_string):
    #parse numpy date string
    date_time = date_string.split('T')
    date_parts = date_time[0].split('-')
    time_parts = date_time[1][:-1].split(':')
    #convert string values to ints
    datetime_ints = [int(d) for d in date_parts] + [int(time_parts[0])]
    
    #apply formatting
    return dt.datetime(*datetime_ints).strftime('%Y-%m-%d')


def prepare_month_ranges(start, end):
    start, end = dateRange(start, end)
    month_ranges = []
    for s, e in zip(start, end):
        month_ranges.append( (s, e) )
    return month_ranges



def count_quakes(start, end):
    over_limit_ranges = []
    month_ranges = prepare_month_ranges(start, end)
    for range in month_ranges:
        fetcher = uf.USGSFetcher('fdsnws', starttime=range[0], endtime=range[1], count=True)
        res = fetcher.exportData()
        print("Zakres dat: ", range, "Count:", res)
        if res > 20000:
            over_limit_ranges.append(range)
            print("!!!!!!!!!!!!!!!!!!!ZA DUŻO!!!!!!!!!!!!!!!!!!!!!")
    
    print(over_limit_ranges)


def split_date_range(start, end, intv):
    """Divide a date range into intervals"""
    from datetime import datetime
    start = datetime.strptime(start,"%Y-%m-%d")
    end = datetime.strptime(end,"%Y-%m-%d")
    diff = (end  - start ) / intv
    for i in range(intv):
        yield (start + diff * i).strftime("%Y-%m-%d")
    yield end.strftime("%Y-%m-%d")


def over_limit_ranges_count():
    ranges = [('2010-04-01', '2010-04-30'), ('2018-06-01', '2018-06-30'), ('2018-07-01', '2018-07-31'), ('2019-07-01', '2019-07-31'), ('2020-06-01', '2020-06-30')]

    for r in ranges:

        date_ranges_in_month = []
        half_of_range = list(split_date_range(r[0], r[1], 2))[1]
        half_of_range_plus_1_day = datetime.strptime(half_of_range,"%Y-%m-%d")
        half_of_range_plus_1_day += timedelta(days=1)
        half_of_range_plus_1_day = half_of_range_plus_1_day.strftime("%Y-%m-%d")

        first_range = (r[0], half_of_range)
        second_range = (half_of_range_plus_1_day, r[1])
        date_ranges_in_month.append(first_range)
        date_ranges_in_month.append(second_range)

        for dt in date_ranges_in_month:
            fetcher = uf.USGSFetcher('fdsnws', starttime=dt[0], endtime=dt[1], count=True)
            res = fetcher.exportData()
            print("Zakres dat: ", dt, "Count:", res)
            if res > 20000:
                date_range_splitted = []
                print('meh')
                print(dt[0], dt[1])
                print(list(split_date_range(dt[0], dt[1], 2)))
                half_of_range = list(split_date_range(dt[0], dt[1], 2))[1]
                half_of_range_plus_1_day = datetime.strptime(half_of_range,"%Y-%m-%d")
                half_of_range_plus_1_day += timedelta(days=1)
                half_of_range_plus_1_day = half_of_range_plus_1_day.strftime("%Y-%m-%d")
                fr = (r[0], half_of_range)
                sr = (half_of_range_plus_1_day, r[1])
                date_range_splitted.append(fr)
                date_range_splitted.append(sr)
                for dts in date_range_splitted:
                    fetcher = uf.USGSFetcher('fdsnws', starttime=dts[0], endtime=dts[1], count=True)
                    res = fetcher.exportData()
                    print("Zakres dat: ", dts, "Count:", res)




                






# count_quakes(start='2000-01-01', end='2022-11-01')
over_limit_ranges_count()
    


# def test():
#     d=list(split_date_range('2019-07-01', '2019-07-16', 2))
#     print(d)
# test()