from flask import Flask
app = Flask(__name__)
@app.route('/')
def index(): # Index function shows a hello world HTML page
    return '<h1>Hello World!</h1>'
