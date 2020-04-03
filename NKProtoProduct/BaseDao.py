#! python3
# -*- coding:utf-8 -*-
import sqlite3
from sqlite3 import OperationalError
from sqlite3 import Cursor
from datetime import date, datetime

class SQLiteBaseDao:
    #connection instance
    __conn = None
    #cursor instance
    __cursor = None
    
    def connectDb(self, dbfilename):
        self.__conn = sqlite3.connect(dbfilename)
        self.__cursor = conn.cursor()
        
    def beginTransaction(self):
        
    
    def select(self, statement, param):
        try:
            c.execute('select * from weather')
        except OperationalError as operr:
            createTable = 'CREATE TABLE weather (id INTEGER PRIMARY KEY AUTOINCREMENT, t timestamp, temperature REAL, pressure REAL, humidity REAL )'
            c.execute(createTable)
        except Exception:
            conn.rollback()
        finally:
            pass        