#!python3
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import urllib.parse

'''
  This soure code is a sample of using pandas library.
  Reading from external file to DataFrame.
'''

#Method of CSV Reading
df = pd.read_csv("./201704health.csv", encoding="utf-8")
print("read csv")
print(df.head(4))
print("")

#Method of Excel Reading
#caution: excel reading dpends on not only pandas but also xlrd.
df = pd.read_excel("./201704health.xlsx")
print("read excel")
print(df.head(4))
print("")

#Method of HTML Reading
#If web page has table elements, pandas is reading data from table elements.
#These data in table elements are readed as list of Dataframe ( one dataframe is one table ).
# question: If web page has no table, pandas can't read data?
#caution: html reading dpends on not only pandas but also html5lib.
a = urllib.parse.quote('トップレベルドメイン一覧', encoding='utf-8')
result_wiki = pd.read_html("https://ja.wikipedia.org/wiki/" + str(a))
domain_list = result_wiki[4]
print("read html")
print(domain_list.head(4))
print("")

#Method of save file.
#Pandas can save data in Dataframes as file.
#caution: excel saving dpends on not only pandas but also openlyxl, odf, pyexcel-ods packages.
domain_list.to_csv('./domain_list.csv')
domain_list.to_excel('./domain_list.xlsx')
domain_list.to_excel('./domain_list.ods')
domain_list.to_pickle('./domain_list.pickle')

