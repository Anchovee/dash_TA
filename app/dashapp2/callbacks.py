import pandas
from datetime import datetime as dt

import plotly.graph_objects as go
import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output

def register_callbacks(dashapp):
    @dashapp.callback(Output('my-graph', 'figure'),[Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        df = pdr.get_data_yahoo(selected_dropdown_value, start=dt(2020, 6, 1), end=dt.now())
        
        df.sma20 = df.Close.rolling(window=20).mean()
        df.stddev = df.Close.rolling(window=20).std()
        df.lower_band = df.sma20 - (2 * df.stddev)
        df.upper_band = df.sma20 + (2 * df.stddev)

        df.TR = abs(df.High - df.Low)
        df.ATR= df.TR.rolling(window=20).mean()

        df.lower_keltner = df.sma20 - (df.ATR * 1.5)
        df.upper_keltner = df.sma20 + (df.ATR * 1.5)
        #data = [dict(type = 'candlestick', open=df.Open, high=df.High, low=df.Low, close=df.Close,x=df.index,yaxis = 'y2')]
        
        data = go.Candlestick(x=list(df.index), open=list(df.Open), high=list(df.High), low=list(df.Low), close=list(df.Close), name='Candlesticks', visible=True)        
        upper_band = go.Scatter(x=list(df.index), y=list(df.upper_band), name='Upper Bollinger Band', line={'color': 'gray'})
        lower_band = go.Scatter(x=list(df.index), y=list(df.lower_band), name='Lower Bollinger Band', line = {'color': 'gray'})
        upper_keltner = go.Scatter(x=list(df.index), y=list(df.upper_keltner), name= 'Upper Keltner', line={'color':'red'})
        lower_keltner = go.Scatter(x=list(df.index), y=list(df.lower_keltner), name= 'Lower Keltner', line={'color':'red'})
        sma20 = go.Scatter(x=list(df.index), y=list(df.sma20), name= '20sma', line={'color':'green'})
        return {
            
            'data': [data, upper_band, lower_band, upper_keltner, lower_keltner, sma20],
            'layout': {
                'xaxis': {
                    'rangeslider': {'visible': False},
                    'type': 'category',
                },

                'margin': {'l': 40, 'r': 0, 't': 20, 'b': 30},
                },
        }
   
    

        

