import os, csv, sys
import yfinance as yf
import pandas as pd
import datetime

from patterns import patterns
from flask import Blueprint, redirect, render_template, request, url_for, Flask
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.urls import url_parse

from app.extensions import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    return render_template("index.html", title='Home Page')


@server_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            error = 'Invalid username or password'
            return render_template('login.html', form=form, error=error)

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@server_bp.route('/logout/')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))


@server_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.login'))

    return render_template('register.html', title='Register', form=form)
# @server_bp.route('/patterns/', methods=['GET', 'POST'])
# def stinkies():
#     if current_user.is_authenticated:
#         return {"success": "route"}

# @server_bp.route('/patterns/', methods=['GET', 'POST'])
# def patterns():
#     if current_user.is_authenticated:
#         pattern = request.args.get('pattern', None)##gets the route func value pair and passes pattern string to variable 
#         stocks = {} #dictionary symbol and bullish/bearish-signal

#         with open('datasets/companies.csv') as f:
#             for row in csv.reader(f):
#                 stocks[row[0]] = {'company': row[1]} #splits symbol dict into new dict symbol = {'company': company name}
#                 #print(stocks)                        #stocks index[index[0] of csv.reader] #'PRU': {'company': 'Prudential Financial'},

#         if pattern:
#             datafiles = os.listdir('datasets/daily') ##get the directory of stock data
#             bullish = []
#             bearish = []
#             for filename in datafiles:
#                 df = pd.read_csv('datasets/daily/{}'.format(filename))
#                 pattern_function = getattr(talib, pattern) #on talib all the functions are named attributes, pass name of function into a variable to call the function
                
#                 symbol = filename.split('.')[0]#takes CSV filenames and gets 1st element of list
#                 try:
#                     result = pattern_function(df['Open'], df['High'], df['Low'], df['Close']) 
                    
#                     last = result.tail(1).values ##get's the last pattern
                    
                
#                     ###bullish/bearish algo 42:09 getting sleepy here
#                     if last > 0:
#                         stocks[symbol][pattern] = 'bullish'
#                         bullish.append(symbol)
#                         # print(symbol)
#                     elif last < 0:
#                         stocks[symbol][pattern] = 'bearish'
#                         bearish.append(symbol)
#                         # print(symbol)
#                     else:
#                         stocks[symbol][pattern] = None
#                         #print("{} triggered {}".format(filename, pattern)) 
#                 except:
#                     pass
            

#         return render_template("charts.html", title="sharts", patterns=patterns, stocks = stocks, current_pattern = pattern) #inserting into body #late add (42:43)#send pattern name to template and url in line(16)(43:43)

# @server_bp.route('/snap/', methods=['GET', 'POST'])
# def snapshot():
#     if current_user.is_authenticated:
#         path = 'datasets/daily'
#         daily_folder = os.listdir(path)
        
#         if len(daily_folder) != 0:
#             for file in daily_folder:
#                 os.remove(os.path.join(path, file))

#         today = datetime.date.today()

#         start = input("Enter start date as YYYY-MM-DD  ")
#         end = today
#         with open('datasets/companies.csv') as f: #get list of company symbols
#             companies = f.read().splitlines()
#             for company in companies:
#                 symbol = company.split(',')[0]
#                 #df = yf.download(symbol, start="2020-07-01", end="2020-11-20") #yf---returns pandas data frame
#                 df = yf.download(symbol, start, end)
#                 df.to_csv('datasets/daily/{}.csv'.format(symbol))
#         return {
#             "code" : "success"
#         }