# coding: utf-8
# flask can run that server daemon. please run from console below
# FLASK_APP=minimumset.py FLASK_ENV=development flask run
from flask import Flask, url_for
app = Flask(__name__)
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): 
    return url_for('profile', username=username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

#result
#/
#/login
#/login?next=/
#/user/John%20Doe

if __name__ == '__main__':
    app.run()
