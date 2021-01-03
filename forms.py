import csv, os
from patterns import patterns

from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import PasswordField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    remember_me = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class Form(FlaskForm):  
    state = SelectField('state', choices=patterns)
    # state = SelectField('state', choices=[('CAr', 'Cauliflower'), ('NVd', 'Nevada'), ('V','Visa')]
    city = SelectField('city', choices=[])

class Candles(FlaskForm):
     pattern = SelectField('pattern', choices=patterns)
