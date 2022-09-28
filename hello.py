from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index(): # Index function shows a hello world HTML page
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<user_name>') # display custom hello message with user name on user page
def user(user_name):
    return render_template('user.html', user_name=user_name)
