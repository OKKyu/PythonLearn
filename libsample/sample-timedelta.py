#! python3
# -*- coding:utf-8 -*-

from datetime import timedelta, datetime

#create timedelta.
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

#manipultate time.
print("now - 1 day = " + str(datetime.now() - timedelta(days=1)))
print("now + 30 seconds = " + str(datetime.now() + timedelta(seconds=30)))
print("now + 10 minutes = " + str(datetime.now() + timedelta(minutes=10)))

#available timedelta's range.
#if we want to initialize datetime, may be available min or max.
print(timedelta.min)
print(timedelta.max)