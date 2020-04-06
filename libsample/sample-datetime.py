#! python3
# -*- coding:utf-8 -*-
from datetime import datetime,timedelta,timezone

jst = timezone(timedelta(hours=9))
today = datetime.now(jst)
print(today)
print(today.year)
print(today.month)
print(today.hour)
print(today.minute)
print(today.second)
#converting from datetime to formatted string.
print("today:" + datetime.strftime(today, "%Y/%m/%d %H:%M:%S"))

#converting from datestring to datetime.
day = datetime.strptime("2030/01/10 06:02:19", "%Y/%m/%d %H:%M:%S")
print(day)