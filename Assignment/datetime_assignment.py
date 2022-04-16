# Assignment to find in which place the sun rises first.
# Get the time zone of 3 different countries and compare with GMT. The closest one to GMT is the place where the sun rises first

import datetime
import pytz

def convertStr_toDateTime(str_date):
    return datetime.datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    
def TimeZone_Difference(date):
    timeZonediff = date[-5:]
    timeZonediff = int(timeZonediff[:timeZonediff.find(':')])
    return timeZonediff

tz1 = 'America/Argentina/Ushuaia'
tz2 = 'Brazil/DeNoronha'
tz3 = 'Jamaica'
str_datetime = '2019-05-15 12:00:00'


l_date_time = convertStr_toDateTime(str_datetime)
#Zone 1
# Assign current Date to EST TimeZone
tz1_TimeZone = pytz.timezone(tz1)
tz1_date = tz1_TimeZone.localize(l_date_time)
FirstZoneDiff = TimeZone_Difference(str(tz1_date))

print("Zone Info:",tz1_TimeZone)
print("Zone Info:",tz1_date.tzinfo)
print("DateTime Info in Zone 1:",tz1_date)
print("Time Difference:",FirstZoneDiff)

#Zone 2
#l_date_time = convertStr_toDateTime(str_datetime)
# Assign current Date to EST TimeZone
tz2_TimeZone = pytz.timezone(tz2)
tz2_date = tz2_TimeZone.localize(l_date_time)
SecondZoneDiff = TimeZone_Difference(str(tz2_date))

print("Zone Info:",tz2_TimeZone)
print("Zone Info:",tz2_date.tzinfo)
print("DateTime Info in Zone 1:",tz2_date)
print("Time Difference:",SecondZoneDiff)

#Zone 1
#l_date_time = convertStr_toDateTime(str_datetime)
# Assign current Date to EST TimeZone
tz3_TimeZone = pytz.timezone(tz3)
tz3_date = tz3_TimeZone.localize(l_date_time)
ThirdZoneDiff = TimeZone_Difference(str(tz3_date))

print("Zone Info:",tz3_TimeZone)
print("Zone Info:",tz3_date.tzinfo)
print("DateTime Info in Zone 1:",tz3_date)
print("Time Difference:",ThirdZoneDiff)

mininum = min(tz1_date,tz2_date,tz3_date)
print("Sun rises first in:", mininum)
"""
l_date_time = datetime.datetime.strptime(str_datetime, '%Y-%m-%d %H:%M:%S')
# Assign current Date to EST TimeZone
tz1_TimeZone = pytz.timezone(tz1)
tz1_date = tz1_TimeZone.localize(l_date_time)
tz1_time = str(tz1_date)
tz1_timeZonediff = tz1_time[-5:]
tz1_timeZonediff = int(tz1_timeZonediff[:tz1_timeZonediff.find(':')])

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
print(tz1_time)
print(tz1_timeZonediff)

print(tz2_TimeZone)
print(tz2_date.tzinfo)
print(tz2_date)

print(tz3_TimeZone)
print(tz3_date.tzinfo)
print(tz3_date)

print(min(1,3,5))
"""