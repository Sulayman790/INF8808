
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file is the entry point for our dash app.
'''

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import pandas as pd

import preprocess
import heatmap
import line_chart
import template


app = dash.Dash(__name__)
app.title = 'TP3 | INF8808'

dataframe = pd.read_csv('./assets/data/arbres.csv')

dataframe = preprocess.convert_dates(dataframe)
dataframe = preprocess.filter_years(dataframe, 2010, 2020)
yearly_df = preprocess.summarize_yearly_counts(dataframe)
data = preprocess.restructure_df(yearly_df)

template.create_custom_theme()
template.set_default_theme()

app.layout = html.Div(className='content', children=[
    html.Header(children=[
        html.H1('Trees planted in Montreal neighborhoods'),
        html.H2('From 2010 to 2020')
    ]),
    html.Main(className='viz-container', children=[
        dcc.Graph(
            id='heatmap',
            className='graph',
            figure=heatmap.get_figure(data),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        ),
        dcc.Graph(
            id='line-chart',
            className='graph',
            figure=line_chart.get_empty_figure(),
            config=dict(
                scrollZoom=False,
                showTips=False,
                showAxisDragHandles=False,
                doubleClick=False,
                displayModeBar=False
            )
        )
    ])
])


@app.callback(
    Output('line-chart', 'figure'),
    [Input('heatmap', 'clickData')]
)
def heatmap_clicked(click_data):
    '''
        When a cell in the heatmap is clicked, updates the
        line chart to show the data for the corresponding
        neighborhood and year. If there is no data to show,
        displays a message.

        Args:
            The necessary inputs and states to update the
            line chart.
        Returns:
            The necessary output values to update the line
            chart.
    '''
    if click_data is None or click_data['points'][0]['z'] == 0:
        fig = line_chart.get_empty_figure()
        line_chart.add_rectangle_shape(fig)
        return fig

    arrond = click_data['points'][0]['y']
    year = click_data['points'][0]['x']

    line_data = preprocess.get_daily_info(
        dataframe,
        arrond,
        year)

    line_fig = line_chart.get_figure(line_data, arrond, year)

    return line_fig
