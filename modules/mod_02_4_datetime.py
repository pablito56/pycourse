#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
MOD: datetime and time
"""

import time


# Current time in seconds since EPOCH. Precission depends on the system.
print time.time()


# Current GMT / UTC time tuple
print time.gmtime()
# Current local time tuple
print time.localtime()


# Both accept an optional argument
print time.gmtime(1368814820)
print time.localtime(1368814820)  # Notice how localtime adds the timezone offset


# This way, to find out which epoch is used (it depends on the system)
print time.gmtime(0)

# It is possible to convert time tuples to seconds since epoch
print time.mktime(time.localtime())
print time.mktime((2013, 5, 17, 20, 20, 20, 4, 137, 1))

# Note how the last value determines whether the timezone offset must be added
print time.mktime((2013, 5, 17, 20, 20, 20, 4, 137, 0))


# Human readable time
print time.ctime()
print time.strftime("%Y/%m/%d %H:%M:%S %Z")
print time.strftime("%Y/%m/%d %H:%M:%S %Z", (2013, 5, 17, 20, 20, 20, 4, 137, 0))


# And read time strings
print time.strptime("2013/05/17 20:20:20 CET", "%Y/%m/%d %H:%M:%S %Z")


import datetime  # More focused to parsing and manipulating


now = datetime.datetime.now()
utcnow = datetime.datetime.utcnow()
print type(now), now
print type(utcnow), utcnow


# More accessible objects
print now.hour
print now.minute
print now.second
print now.microsecond
print now.year
print now.month
print now.day
print now.weekday()
print now.isoweekday()
print now.timetuple()  # Useful with time.mktime


# Humand readable output and input
print utcnow.strftime("%Y/%m/%d %H:%M:%S %Z")
print utcnow.isoformat()
print repr(datetime.datetime.strptime("2013/05/17 20:20:20 CET", "%Y/%m/%d %H:%M:%S %Z"))


# There are more classes in the datetime module
print datetime.time(20, 20, 20)
print datetime.date.today()


# It is possible to operate with datetime, time and date objects
diff = datetime.datetime.now() - datetime.datetime.utcnow()
print type(diff), diff
print datetime.datetime.strptime("2013/05/17 20:20:20 CET", "%Y/%m/%d %H:%M:%S %Z") - diff

diff = datetime.date.today() - datetime.date(2013, 05, 17)
print datetime.date(*time.gmtime(0)[:3]) + diff + datetime.timedelta(weeks=6, days=4)


# What about the timezone?
print now.tzinfo


#===============================================================================
# Timezone is not provided by default. It must be managed manually with a subclass
# of datetime.tzinfo. Check the standard library documentation for examples, or use
# a 3rd party library like pytz (recommended): http://pytz.sourceforge.net/
#===============================================================================


# Let's deal with http timestamps
gmt = "Fri, 17 May 2013 11:49:45 GMT"


# how would you get the epoch time?
time_obj = time.strptime(gmt, '%a, %d %b %Y %H:%M:%S %Z')


# and now...time.mktime()?
time.mktime(time_obj)


# but...
time.gmtime(time.mktime(time_obj))
time.gmtime(time.mktime(time_obj))


# time.mktime is the inverse function for time.localtime
# use calendar.timegm for getting the time in epoch
import calendar
time.gmtime(calendar.timegm(time_obj))


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/time.html
#  - http://pymotw.com/2/time/
#  - http://docs.python.org/2/library/datetime.html
#  - http://pymotw.com/2/datetime/
#  - http://pytz.sourceforge.net/
#===============================================================================
