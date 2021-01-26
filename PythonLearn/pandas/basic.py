#!python3
# -*- coding:utf-8 -*-

import os
import numpy as np
import pandas as pd

'''
  This source code is a sample of using pandas library.
  Series and DataFrame.
'''

# Series Object: It's one dimension object.
# It's not ndarray, list, and other sequense object.
print("make instance of Series")
ser = pd.Series([10,20,30,40])
print(ser)
ser = pd.Series(np.arange(1,10,2))
print("")

# DataFrame: It's Group of Series Object.
# It's looks like spread sheet.
df = pd.DataFrame([[10,20,30,40],
                   [1,2,3,4],
                   [100,200,300,400]])
print("DataFrame debug.")
print(" if all values have same type that each other values have it, column's dtype is defined to same type automatically.")
print(df)
print("")

df = pd.DataFrame([[10,True,30,None],
                   ["acb",2,{},4],
                   [2.4,200,300,400]])
print(" if any values have different type regard to other values, column's dtype is defined to object type automatically.")
print(df)
print("")

#Overviewing of DataFrame.
# create Dataframe
df = pd.DataFrame(np.arange(100).reshape((25,4)))
print("new dataframe")
print("df.head() is display that top of 10 rows.")
print(df.head(10))
print("df.tail() is display that last of 10 rows.")
print(df.tail(10))
print("dataframe also have shape attribute.")
print("shape :" + str(df.shape))
print("")

#DataFrame with index name and column name.
print("You can alter dataframe with index names after created it.")
print("It also is possible to column names.")
df.index =  [ "\"" + str(x).rjust(2,"0") + "\"" for x in range(df.shape[0]) ]
df.columns = [ chr(x) for x in np.arange(97, 97 + df.shape[1], 1) ]
print("renamed index name and column name.")
print(df)
print("")

print("if you want to naming indice or columns when you create dataframe,")
print("you can code about below...")
df = pd.DataFrame(np.arange(100).reshape((25,4)),
                  index=[ "\"" + str(x).rjust(2,"0") + "\"" for x in range(df.shape[0]) ],
                  columns=[ chr(x) for x in np.arange(97, 97 + df.shape[1], 1) ] )
print(df)
print("")

print("AndAlso, you can create dataframe from dict object, based columns.")
print("If column length is different each other, value error has occured.")
df2 = pd.DataFrame({"ColumnA":[1, 2, 3], "ColumnB":[10, 20, 30]})
df2.index = ["１行目", "２行目", "３行目"]
print(df2)
print("")

#Data Extraction
print("select by column name: df2['ColumnA']")
print(df2['ColumnA'])
print("")
print("select by column name both: df2[['ColumnA', 'ColumnB']]")
print(df2[['ColumnA', 'ColumnB']])
print("")

#DataFrame can use slicing as list object.
print("slicing dataframe [:1]")
print(df2[:1])
print("")

#DataFrame provides other extraxting methods, loc and iloc.
print("loc[ slice_row_name, slice_column_name  ]")
print(df2.loc[:"３行目", : ])
print(df2.loc[:"２行目", "ColumnB" ])
print("iloc[ slice_row_index, slice_column_index  ]")
print(df2.iloc[:3, : ])
print(df2.iloc[:2, 1])
print("")
