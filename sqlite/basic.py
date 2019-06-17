#! python3
# -*- coding:utf-8 -*-

import sqlite3
conn = sqlite3.connect('example.db')
#conn = sqlite3.connect(':memory:')

c = conn.cursor()
#c.execute('drop table test')
c.execute('create table test (id text, comment text, ctime text, utime text)')
c.execute('insert into test values (\'001\',\'test insert\',\'aaa\',\'bbb\')')
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
