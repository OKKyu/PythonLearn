# coding: utf-8
# flask can run that server daemon. please run from console bellow
#    FLASK_APP=minimumset.py FLASK_ENV=development
#    flask run
import socket
from pathlib import Path
from flask import Flask, request
app = Flask(__name__)

@app.route('/moistinfo', methods=['POST'])
def moistinfo():
    sendedIP = request.remote_addr
    #moistpoint = request.form["VCC"]
    #app.logger.debug("value:" + str(moistpoint))
    app.logger.debug("data send from:" + str(sendedIP))
    app.logger.debug("data point:" + str(request.json["VCC"]))
    app.logger.debug("receive ok to " + socket.gethostname())
    
    return "receive ok to " + socket.gethostname()

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', debug=True, port=5001)
