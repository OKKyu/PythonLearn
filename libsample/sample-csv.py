#!python3
# -*- coding:utf-8 -*-
import csv

with open('top_cities.csv','w', encoding='utf-8') as f:
    #open writer. first arg is target file object.
    writer = csv.writer(f)
    #write row. argument allowed list,tuple.
    writer.writerow(['rank','city','population'])
    # write multi rows.
    writer.writerows([
            [1,'aaa',121],
            [2,'aab',0],
            [3,'aac',931]
        ])
    
with open('top_cities_2.csv','w', encoding='utf-8') as f:
    #open writer. first arg is target file object. 2nd arg is list of header field names.
    writer = csv.DictWriter(f,['rank','city','population'])
    #write header line.
    writer.writeheader()
    # write multi rows.
    writer.writerows([
            { 'rank':1, 'city':'aaa', 'population': 121 },
            { 'rank':2, 'city':'aab', 'population': 0 },
            { 'rank':3, 'city':'aac', 'population': 1232 }
        ])
