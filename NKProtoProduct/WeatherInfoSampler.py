#! python3
# -*- coding:utf-8 -*-
# 温度センサーモジュール（BME280）による気候情報のサンプリングを行うプログラム。
# 1)ラズベリーパイが設置された環境の温度、湿度、気圧をセンサーにより取得する。情報はタプル形式の返却値で取得する。
# 2)データベースへ情報を保存する。データベースはsqliteを使用する。
#    database WeatherInfo
#    table Location
#    table weather
# 3)本プログラムは上記処理を１回実行すると終了する。
#   定期的に繰り返し情報を取得させたい場合はOSのスケジューラを使用して本プログラムを実行させる仕様とする。

import sqlite3
from sqlite3 import OperationalError
from sqlite3 import Cursor
import re
import sys,traceback
from datetime import date, datetime
#from BME280.Python27 import bme280

class WeatherInfoSampler():
    
    def __init__(self):
        if sys.version_info.major <= 2:
            pass
        
    #mode 0:sampling only, 1: sampling and displaying
    def samplingWeather(self, mode=0):
        conn = None
        try:
            conn = self.__connectDb__()
            #info = self.__getInfo__()
            info = [12,34,56.00]
            self.__save__(conn.cursor(),info,mode)
            conn.commit()
        except Exception:
            conn.rollback()
            sys.stderr.write(traceback.format_exc())
        finally:
            conn.close()

    def loadInfo(self, id=None, t=None, temp=None, press=None, hum=None):
        conn = None
        try:
            conn = self.__connectDb__()
            cursor = conn.cursor()
            
            searchCondition = {}
            if id is not None and type(id) is int:
                searchCondition["id"] = id
            if t is not None and type(t) is int:
                searchCondition["time"] = t
            if temp is not None and type(temp) is float:
                searchCondition["temp"] = temp
            if press is not None and type(press) is float:
                searchCondition["press"] = press
            if hum is not None and type(hum) is float:
                searchCondition["hum"] = hum
            
            statement = 'select * from weather '
            if len(searchCondition) != 0:
                statement = statement + 'where'
                cnt = 1
                for key in searchCondition:
                    statement = statement + " " + key + "=" + str(searchCondition[key]) + " "
                    if cnt != len(searchCondition):
                        statement = statement + "and"
                        
            for info in cursor.execute(statement):
                print(info)
            
        except Exception:
            conn.rollback()
            sys.stderr.write(traceback.format_exc())
        finally:
            conn.close()

    def __connectDb__(self):
        conn = sqlite3.connect('WeatherInfo')
        c = conn.cursor()
        try:
            c.execute('select * from weather')
        except OperationalError as operr:
            createTable = 'CREATE TABLE weather (id INTEGER PRIMARY KEY AUTOINCREMENT, t timestamp, temperature REAL, pressure REAL, humidity REAL )'
            c.execute(createTable)
        except Exception:
            conn.rollback()
        finally:
            pass
        
        return conn

    def __save__(self, cursor, info, mode):
        if cursor is None or isinstance(cursor,Cursor) == False :
            raise ValueError()
        if info is None or len(info) != 3:
            raise ValueError(('infomation num isn\'t 3.',))
        
        t = datetime.now()
        cursor.execute('insert into weather (t,temperature,pressure,humidity) values (?,?,?,?)', (t,info[0],info[1],info[2]))
        if mode == 1:
            print(str(t) +  " " +str(info))

    def __getInfo__(self):
        bme280.get_calib_param()
        info = bme280.readData()
        return info

if __name__ == '__main__':
    sampler = WeatherInfoSampler()
    sampler.samplingWeather(0)
    sampler.loadInfo()