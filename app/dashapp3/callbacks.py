from datetime import datetime as dt

import pandas_datareader as pdr
from dash.dependencies import Input
from dash.dependencies import Output

from dash.exceptions import PreventUpdate



def register_callbacks(dashapp):
    @dashapp.callback([
    Output('graph', 'figure'),
    Output('data-table', 'data'),
    Output('data-table', 'columns'),
    Output('container', 'style')
], [Input('data-dropdown', 'value')])

    def update_graph(value):
        sample_data = {
            'series': {
                'data': [
                    {'title': 'Game of Thrones', 'score': 9.5},
                    {'title': 'Stranger Things', 'score': 8.9},
                    {'title': 'Vikings', 'score': 8.6}
                ],
                'style': {
                    'backgroundColor': '#ff998a'
                }
            },
            'movies': {
                'data': [
                    {'title': 'Rambo', 'score': 7.7},
                    {'title': 'The Terminator', 'score': 8.0},
                    {'title': 'Alien', 'score': 8.5}
                ],
                'style': {
                    'backgroundColor': '#fff289'
                }
            }
        }
        if value is None:
            raise PreventUpdate
        
        selected = sample_data[value]
        data = selected['data']
        columns = [
            {'name': k.capitalize(), 'id': k}
            for k in data[0].keys()
        ]
        figure = go.Figure(
            data=[
                go.Bar(x=[x['score']], text=x['title'], name=x['title'])
                for x in data
            ]
        )

        return figure, data, columns, selected['style']