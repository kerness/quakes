
# date = "2010/01/07"
# time = "16:19:00.00"

# time = time.split('.')[0]
# dt_string = date + " " + time
# print(dt_string)

# from datetime import datetime


# dt = datetime.strptime(dt_string, "%Y/%m/%d %H:%M:%S")
# print(dt)
# from calendar import timegm
# timestamp = timegm(dt.timetuple())
# print(timestamp)

# def create_timestamp(date, time):
#     """
#     Converts date and time string to UNIX timestamp
#     The date is like: "2010/01/07"
#     The time is like: "16:19:00.00"
#     """
#     from datetime import datetime
#     from calendar import timegm

#     time = time.split('.')[0]
#     dt_string = date + " " + time
#     dt = datetime.strptime(dt_string, "%Y/%m/%d %H:%M:%S")
#     timestamp = timegm(dt.timetuple())

#     return timestamp

# print(create_timestamp(date, time))

from GRSSfetcher import GRSSFetcher

f = GRSSFetcher()
f.exportData()