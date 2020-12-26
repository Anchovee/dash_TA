import os, csv, pandas
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas_datareader as pdr

from datetime import datetime as dt
# layout = html.Div([
#     html.H1('Stick Tockers'),
#     dcc.Dropdown(
#         id='my-dropdown',
#         options=[
#             {'label': 'AMD', 'value': 'AMD'},
#             {'label': 'Tesla', 'value': 'TSLA'},
#             {'label': 'Apple', 'value': 'AAPL'}
#         ],
#         value='COKE'
#     ),
#     dcc.Graph(id='my-graph')
# ], style={'width': '500'})

# def in_squeeze(df):
#     df.sma20 = df.Close.rolling(window=20).mean()
#     df.stddev = df.Close.rolling(window=20).std()
#     df.lower_band = df.sma20 - (2 * df.stddev)
#     df.upper_band = df.sma20 + (2 * df.stddev)

#     df.TR = abs(df.High - df.Low)
#     df.ATR= df.TR.rolling(window=20).mean()

#     df.lower_keltner = df.sma20 - (df.ATR * 1.5)
#     df.upper_keltner = df.sma20 + (df.ATR * 1.5)
#     return df.lower_band > df.lower_keltner and df.upper_band < df.upper_keltner

# stocks = []
# '''get stock symbols'''
# with open('datasets/companies.csv') as f:
#     for row in csv.reader(f):
#         key = {'label': row[0],'value': row[0]}
#         stocks.append(key)

stocks = []
with open('datasets/squeeze.csv') as f:
    for row in csv.reader(f):
        symbol = {'label':  row[0] +', '+row[1],'value': row[0]}
        stocks.append(symbol)
        

layout = html.Div([
    html.H1('Squeeze Breakouts'),
    dcc.Dropdown(
        id='my-dropdown',
        options=stocks,
        value='COKE'
    ),
    

    dcc.Graph(id='my-graph')
    ], style={'width': '500'})

#checkboxes for different features recent unusual volume, 
# 0-1% sma, double top, news, bullish cross, highest atr/options volume update weekly, 
#tweezer top/bottom

#button to add to a watchlish that tracks strategy and updates weekly with historical analysis