from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm): # define a name form
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index(): # Index function shows a hello world HTML page
    name = None
    form = NameForm() # pass the name form defined earlier to the template
    if form.validate_on_submit(): # check if valid data was submitted
        name = form.name.data
        form.name.data = '' # clear form field
    return render_template('index.html', form=form, name=name)


@app.route('/user/<user_name>') # display custom hello message with user name on user page
def user(user_name):
    return render_template('user.html', user_name=user_name)
