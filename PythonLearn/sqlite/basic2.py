# python3
# -*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('insert into test values (\'001\',\'test insert\',\'aaa\',null)')

# Never do this -- insecure!
#symbol = '001'
#c.execute("SELECT * FROM test WHERE id = '%s'" % symbol)

# Do this instead
t = ('001',)
c.execute('SELECT * FROM test WHERE id=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
inserts = [('002', 'MeisSuper', '20190701', '20190701' ),
             ('003', 'Shaa', '20190701', '20190701' ),
             ('004', 'Deeeh', '20190701', '20190701' ),
            ]
c.executemany('INSERT INTO test VALUES (?,?,?,?)', inserts)

for item in c.execute('SELECT * FROM test'):
    print(item)

c.execute('SELECT * FROM test')
print(c.fetchall())

c.execute('SELECT * FROM test where id=? or id=?',(1,2))
print(c.fetchall())

c.execute('SELECT * FROM test where comment=:comm or ctime=:date ',{'comm':'Deeeh', 'date':'20190701'})
print(c.fetchall())
c.execute('SELECT * FROM test')
print(c.fetchmany(2))

conn.rollback()
conn.close()
