#! python3
# -*- coding:utf-8 -*-

import sqlite3

#デフォルトでは、 sqlite3 モジュールは connect の呼び出しの際にモジュールの Connection クラスを使います。しかし、 
#Connection クラスを継承したクラスを factory パラメータに渡して connect() にそのクラスを使わせることもできます。
#詳しくはこのマニュアルの SQLite と Python の型 節を参考にしてください。
#sqlite3 モジュールは SQL 解析のオーバーヘッドを避けるために内部で文キャッシュを使っています。
#接続に対してキャッシュされる文の数を自分で指定したいならば、 cached_statements パラメータに設定してください。
#現在の実装ではデフォルトでキャッシュされる SQL 文の数を 100 にしています。

#connect database.
conn = sqlite3.connect('example.db')
#create database only on RAM mode.
#conn = sqlite3.connect(':memory:')

#Calling cursor for execute sql statements.
c = conn.cursor()

#SQLite はネイティブで TEXT、INTEGER、REAL、BLOB および NULL のみをサポートしています。その他のタイプを使用したい場合は
#あなた自身で追加しなければなりません。detect_types パラメータおよび、register_converter() 関数でモジュールレベルで
#登録できるカスタム 変換関数 を使用することで簡単に追加できます。
c.execute('create table test (id integer, comment text, ctime REAL, tmpimage BLOB)')

#commiting executed DML, DDL
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
