# Assignment to find in which place the sun rises first.
# Get the time zone of 3 different countries and compare with GMT. The closest one to GMT is the place where the sun rises first

import datetime
import pytz

tz1 = 'America/Argentina/Ushuaia'
tz2 = 'Brazil/DeNoronha'
tz3 = 'Jamaica'

str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
# Assign current Date to EST TimeZone
tz1_TimeZone = pytz.timezone(tz1)
tz1_date = tz1_TimeZone.localize(l_date_time)

str_datetime = '2019-05-15 12:00:00'
l_date_time1 = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
# Assign current Date to EST TimeZone
tz2_TimeZone = pytz.timezone(tz2)
tz2_date = tz2_TimeZone.localize(l_date_time1)

str_datetime = '2019-05-15 12:00:00'
l_date_time2 = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
# Assign current Date to EST TimeZone
tz3_TimeZone = pytz.timezone(tz3)
tz3_date = tz3_TimeZone.localize(l_date_time2)

print(tz1_TimeZone)
print(tz1_date.tzinfo)
print(tz1_date)

print(tz2_TimeZone)
print(tz2_date.tzinfo)
print(tz2_date)

print(tz3_TimeZone)
print(tz3_date.tzinfo)
print(tz3_date)
