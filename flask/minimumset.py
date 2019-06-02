# coding: utf-8
# flask can run that server daemon. please run from console bellow
# FLASK_APP=minimumset.py FLASK_ENV=development flask run

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"
    
@app.route("/renderSample")
def renderSample():
    name ="ME!"
    return render_template("index.html", name=name)

@app.route('/user/<username>')
def show_user_name(username):
    return "inputed user name is...." + username

@app.route('/plus/<int:numb>')
def calcPlus(numb):
    numb = numb + 4
    return str(numb)

if __name__ == '__main__':
    app.run()
