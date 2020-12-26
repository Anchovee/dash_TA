import os, csv
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
import dash_table as dt

layout = html.Div([
    html.H1('Multi output example'),
    dcc.Dropdown(id='data-dropdown', options=[
        {'label': 'Movies', 'value': 'movies'},
        {'label': 'Series', 'value': 'series'}
    ], value='movies'),
    html.Div([
        dcc.Graph(id='graph'),
        dt.DataTable(id='data-table', columns=[
            {'name': 'Title', 'id': 'title'},
            {'name': 'Score', 'id': 'score'}
        ])
    ])
], id='container')

#checkboxes for different features recent unusual volume, 
# 0-1% sma, double top, news, bullish cross, highest atr/options volume update weekly, 
#tweezer top/bottom

#button to add to a watchlish that tracks strategy and updates weekly with historical analysis