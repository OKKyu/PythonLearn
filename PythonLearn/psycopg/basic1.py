#!python3
# -*- coding:utf-8 -*-
# This code is reffered from below.
# https://resanaplaza.com/2021/09/08/%e3%80%90-python-%e3%80%91psycopg2%e3%81%a7postgresql%e3%81%ab%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b9%e3%81%97%e3%82%88%e3%81%86%ef%bc%81/

import sys
import psycopg2

# step1: make connection string.
connection_str = {}
connection_str.setdefault('host', sys.argv[1])
connection_str.setdefault('port', sys.argv[2])
connection_str.setdefault('dbname', sys.argv[3])
connection_str.setdefault('user', sys.argv[4])
connection_str.setdefault('password', sys.argv[5])

constr = ""

for key, value in connection_str.items():
    constr += key + "=" + value + " "

try:
    # step2: connecting.
    conn = psycopg2.connect(constr)

    # step3: get cursor.
    cur = conn.cursor()
    cur.

    # step4: run sql with execute method.
    #          execute can DML and DDL.
    # cur.execute('insert into hoge(id,tag,cost) values('10001','ABCD',120)'))
    if len(sys.argv) >= 7:
        cur.execute('SET search_path TO ' + sys.argv[6])
    cur.execute('select * from departments')
    for item in cur.fetchall():
        print(item)
    # other, you can use res.fetchall(), res.fetchmeny(num).

    # step5: run commit or rollback.
    conn.commit()

except Exception as ex:
    conn.rollback()
    print(ex)
finally:
    # step6: after process (closing connection).
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
