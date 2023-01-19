import numpy as np
import datetime as dt


def dateRange(start="2000-01-01", end="2000-12-31"):
    # https://stackoverflow.com/questions/63637444/python-month-start-and-end-dates-between-two-dates
    start_date = np.datetime64(start[:-3])
    # Add one month to end date so last month is included
    end_date = np.datetime64(end[:-3]) + np.timedelta64(1, "M")
    # Create Date Range
    date_range = np.arange(start_date, end_date, dtype="datetime64[M]")
    # Add 5 AM to start_dates
    start_dates = date_range + np.timedelta64(5, "h")
    # Add 1 Month and subrtract 4 hours to 8 PM on last day of month
    end_dates = date_range + np.timedelta64(1, "M") - np.timedelta64(4, "h")
    # Apply Formatting
    final_start_dates = [
        parse_date(np.datetime_as_string(d, unit="s")) for d in start_dates
    ]
    final_end_dates = [
        parse_date(np.datetime_as_string(d, unit="s")) for d in end_dates
    ]

    return final_start_dates, final_end_dates


def parse_date(date_string):
    # parse numpy date string
    date_time = date_string.split("T")
    date_parts = date_time[0].split("-")
    time_parts = date_time[1][:-1].split(":")
    # convert string values to ints
    datetime_ints = [int(d) for d in date_parts] + [int(time_parts[0])]

    # apply formatting
    return dt.datetime(*datetime_ints).strftime("%Y-%m-%d")


def prepare_month_ranges(start, end):
    start, end = dateRange(start, end)
    month_ranges = []
    for s, e in zip(start, end):
        month_ranges.append((s, e))
    return month_ranges


def split_date_range(start, end, intv):
    """Divide a date range into intervals"""
    from datetime import datetime

    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    diff = (end - start) / intv
    for i in range(intv):
        yield (start + diff * i).strftime("%Y-%m-%d")
    yield end.strftime("%Y-%m-%d")
