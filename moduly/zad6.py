import time
print(time.time())

print(time.localtime())

print(time.localtime().tm_year)

import calendar
print(calendar.month(2022,11,w=5,l=2))
print(calendar.isleap(2022))
print(calendar.calendar(2022))

print(time.localtime().tm_hour, time.localtime().tm_mday, time.localtime().tm_mon, time.localtime().tm_year)

print(calendar.month(2001,4))
calendar.setfirstweekday(6)
print(calendar.month(2001,4))
print(calendar.isleap(2000))
print(calendar.calendar(2019))
