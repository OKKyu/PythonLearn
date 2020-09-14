#!python3
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas.
  Date table.
'''

#date_range methods create DatetimeIndex object.
dates = pd.date_range(start="2020-04-01", end="2020-04-30")
print("date_range was created: start:" + "2020-04-01" + "  " + "2020-4-30")
print(dates)
print("")

#DatetimeIndex object is used to index of DataFrame.
df = pd.DataFrame(np.random.randint(100, 10000, 30), index=dates, columns=["step per day"])
print("dataframe that used by dates with index.")
print(df)
print(df.describe())
print("")

# Period of 365 days (1year) is creating.
dates = pd.date_range(start="2020-04-01", periods=365)
print("Period of 365 days (1year) is creating.")
print("start:" +  str(dates.min()) +  " end:" + str(dates.max()))
df = pd.DataFrame(np.random.randint(100, 10000, 365), index=dates, columns=["step per day"])
print(df.head(5))
print(df.tail(5))
print("")

#Summerizing by grouping. It's able to use like group by of sql.
#Mean of each Months.
print("group by Month and mean")
print(df.groupby(pd.Grouper(freq="M")).mean())
#Max of each Months.
print("group by Month and max")
print(df.groupby(pd.Grouper(freq="M")).max())
print("")

#date_range can also create dates that contains only particular day of week.
#freq=W-SAT indicate saturday.
w_sat = pd.date_range(start="2020-04-01", end="2021-03-31", freq="W-SAT")

#You can recreate new dataframe that was filterd by particular day of week.
df_sat_in_year = pd.DataFrame(df.groupby(pd.Grouper(freq="W-SAT")).sum(), index=w_sat, columns=["step per day"])
print("saturday only data")
print(df_sat_in_year)
print("")