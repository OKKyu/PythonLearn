#! python3
# coding: utf-8
# flask can run that server daemon. please run from console bellow
#    FLASK_APP=minimumset.py FLASK_ENV=development
#    flask run
import socket
from pathlib import Path
import datetime
from flask import Flask, request
import sqlite3 as sqlite

#initialize
app = Flask(__name__)
conn = __connectDb__()    

@app.route('/moistinfo', methods=['POST'])
def moistinfo():
    sendedIP = request.remote_addr
    app.logger.debug("data send from:" + str(sendedIP))
    app.logger.debug("data point:" + str(request.json["VCC"]))
    app.logger.debug("receive ok to " + socket.gethostname())
    
    if conn is not None:
        __saveMoistInfo(sendedIP,request.json["VCC"])
    
    return "receive ok to " + socket.gethostname()

def __connectDb__():
    conn = sqlite3.connect('MoistInfo.db')
    c = conn.cursor()
    try:
        c.execute('select * from moist')
    except OperationalError as operr:
        createTable = 'CREATE TABLE moist (id INTEGER PRIMARY KEY AUTOINCREMENT, ipaddr TEXT, t timestamp, moistpoint INTEGER )'
        c.execute(createTable)
    except Exception:
        conn.rollback()
        conn.close()
        conn = None
    finally:
        pass
        
    return conn

def __saveMoistInfo(ipaddr, moistpt):
    c = conn.cursor()
    try:
        c.execute('insert into moist (t, ipaddr, moistpoint) values (?,?,?)', (datetime.now(), ipaddr, moistpt))
    except Exception:
        conn.rollback()
        print('failed insert information. rollback.')
    finally:
        conn.commit()
        
if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', debug=True, port=5001)
    if conn is None:
        print('connection is failed. this service isnt save moistinfo... but running.')

