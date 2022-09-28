from flask import Flask
app = Flask(__name__)

@app.route('/')
def index(): # Index function shows a hello world HTML page
    return '<h1>Hello World!</h1>'

@app.route('/user/<user_name>') # display custom hello message with user name on user page
def user(user_name):
    return '<h1>Hello, {}!</h1>'.format(user_name)
