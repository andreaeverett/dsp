# Use Python to compute days between start and stop date.

from datetime import *

# Create 2 lists, one for start dates and the other for end dates
start_dates = []
stop_dates = []

####a) Get the start and end dates for A, and put them in their respective lists
date_start = '01-02-2013'
date_stop = '07-28-2015'

start_a = date_start.split('-')
stop_a = date_stop.split('-')

start_dates.append(start_a)
stop_dates.append(stop_a)

####b) Get the start and end dates for B, and put them in their respective lists
date_start = '12312013'
date_stop = '05282015'

start_b = [date_start[0:2], date_start[2:4], date_start[4:8]]
stop_b = [date_stop[0:2], date_stop[2:4], date_stop[4:8]]

start_dates.append(start_b)
stop_dates.append(stop_b)

####c) Get the start and end dates for C, and put them in their respective lists
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

start_c = date_start.split('-')
stop_c = date_stop.split('-')

# Put them in Month - Day - Year order like the others
month = start_c.pop(1)
start_c.insert(0, month)

month = stop_c.pop(1)
stop_c.insert(0, month)

# Turn the months into strings that can be turned into integers
start_c[0] = start_c[0].replace('Jan', '01')
stop_c[0] = stop_c[0].replace('Jul', '07')

start_dates.append(start_c)
stop_dates.append(stop_c)

# Now put all the dates in the lists in Year - Month - Day order

def date_order(dates):
    for date in dates:
        year = date.pop()
        date.insert(0, year)
    return dates

start_dates = date_order(start_dates)
stop_dates = date_order(stop_dates)

# Now turn the entries into integers
def make_ints(string_dates):
    int_dates = []
    for date in string_dates:
        date = map(int, date)
        int_dates.append(date)
    return int_dates

start_dates = make_ints(start_dates)
stop_dates = make_ints(stop_dates)

# Now turn the dates into date objects defined by (year, month, day)
def make_date_objects(int_dates):
    date_objects = []
    for time in int_dates:
        time = date(*time)
        date_objects.append(time)
    return date_objects

start_dates = make_date_objects(start_dates)
stop_dates = make_date_objects(stop_dates)

# Now find the deltas between the corresponding pairs:
def elapsed_days(begin, end):
    elapsed = []
    for date1, date2 in zip(begin, end):
        elapsed.append(date2-date1)
    return elapsed

answers = elapsed_days(start_dates, stop_dates)
print answers
