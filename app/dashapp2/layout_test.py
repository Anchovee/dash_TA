import os, csv, pandas
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas_datareader as pdr

from datetime import datetime as dt
stocks = []
with open('datasets/squeeze.csv') as f:
    for row in csv.reader(f):
        symbol = {'label': row[0],'value': row[0]}
        stocks.append(symbol)
        

layout = html.Div(children=[
    html.Div([
        html.H1(children='Squeeze Breakouts'),
        
        dcc.Graph(
            id='my-graph'
        ),
    ], style={'width': '500'}),

    html.Div([
        html.H1(children='Squeeze Breakouts'),
        
        dcc.Graph(
            id='my-graph1'
        ),
       
    ], style={'width': '500'})
])
#checkboxes for different features recent unusual volume, 
# 0-1% sma, double top, news, bullish cross, highest atr/options volume update weekly, 
#tweezer top/bottom

#button to add to a watchlish that tracks strategy and updates weekly with historical analysis