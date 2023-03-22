# front facing html page with 10 columns and five rows each equal
# to 1/10th of the screen

import dash 
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table

# import data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# create app
app = dash.Dash()

# create layout
app.layout = html.Div([
    html.Div([
        html.Div([
            html.H1('Gapminder Data'),
            html.P('This is a Dash app that displays the Gapminder data set'),
            html.P('Select a year from the dropdown menu'),
            html.P('Select a column from the dropdown menu'),
            html.P('Select a row from the dropdown menu'),
            html.P('Select a color from the dropdown menu'),
            html.P('Select a size from the dropdown menu'),
            html.P('Select a symbol from the dropdown menu'),
            html.P('Select a text from the dropdown menu'),
            html.P('Select a facet from the dropdown menu'),
            html.P('Select a facet row from the dropdown menu'),
            html.P('Select a facet column from the dropdown menu'),
            html.P('Select a facet color from the dropdown menu'),
            html.P('Select a facet size from the dropdown menu'),
            html.P('Select a facet symbol from the dropdown menu'),
            html.P('Select a facet text from the dropdown menu'),
            html.P('Select a facet facet from the dropdown menu'),
            html.P('Select a facet facet row from the dropdown menu'),
            html.P('Select a facet facet column from the dropdown menu'),
            html.P('Select a facet facet color from the dropdown menu'),
            html.P('Select a facet facet size from the dropdown menu'),
            html.P('Select a facet facet symbol from the dropdown menu'),
            html.P('Select a facet facet text from the dropdown menu'),
            html.P('Select a facet facet facet from the dropdown menu'),
            html.P('Select a facet facet facet row from the dropdown menu'),
            html.P('Select a facet facet facet column from the dropdown menu'),
            html.P('Select a facet facet facet color from the dropdown menu'),

        ], className='three columns'),
        html.Div([
    
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='gdpPercap'
            ),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='lifeExp'
            ),  
            dcc.Dropdown(
                id='color-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='continent'
            ),  
            dcc.Dropdown(
                id='size-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='pop'
            ),
            dcc.Dropdown(
                id='symbol-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='text-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-row-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-column-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-color-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-size-column',
                options=[{'label': i, 'value': i} for i in df.columns], 
                value='country'
            ),
            dcc.Dropdown(
                id='facet-symbol-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-text-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-row-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-column-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-color-column',  
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-size-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-symbol-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-text-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-facet-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-facet-row-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-facet-column-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
            dcc.Dropdown(
                id='facet-facet-facet-color-column',
                options=[{'label': i, 'value': i} for i in df.columns],
                value='country'
            ),
        ], className='three columns'),
        html.Div([
            dcc.Graph(id='indicator-graphic')
        ], className='six columns')
    ], className='row')

    @app.callback(
        Output('indicator-graphic', 'figure'),
        [Input('xaxis-column', 'value'),
            Input('yaxis-column', 'value'),
            Input('color-column', 'value'),
            Input('size-column', 'value'),
            Input('symbol-column', 'value'),
            Input('text-column', 'value'),
            Input('facet-column', 'value'),
            Input('facet-row-column', 'value'),
            Input('facet-column-column', 'value'),
            Input('facet-color-column', 'value'),
            Input('facet-size-column', 'value'),
            Input('facet-symbol-column', 'value'),
            Input('facet-text-column', 'value'),
            Input('facet-facet-column', 'value'),
            Input('facet-facet-row-column', 'value'),
            Input('facet-facet-column-column', 'value'),
            Input('facet-facet-color-column', 'value'),
            Input('facet-facet-size-column', 'value'),
            Input('facet-facet-symbol-column', 'value'),
            Input('facet-facet-text-column', 'value'),
            Input('facet-facet-facet-column', 'value'),
            Input('facet-facet-facet-row-column', 'value'),
            Input('facet-facet-facet-column-column', 'value'),
            Input('facet-facet-facet-color-column', 'value')])
    def update_graph(xaxis_column_name, yaxis_column_name,
                        color_column_name, size_column_name, symbol_column_name, text_column_name,
                        facet_column_name, facet_row_column_name, facet_column_column_name, facet_color_column_name, facet_size_column_name, facet_symbol_column_name, facet_text_column_name,
                        facet_facet_column_name, facet_facet_row_column_name, facet_facet_column_column_name, facet_facet_color_column_name, facet_facet_size_column_name, facet_facet_symbol_column_name, facet_facet_text_column_name,
                        facet_facet_facet_column_name, facet_facet_facet_row_column_name, facet_facet_facet_column_column_name, facet_facet_facet_color_column_name):

        dff = df    

        return {
            'data': [go.Scatter(
                x=dff[dff['country'] == i][xaxis_column_name],
                y=dff[dff['country'] == i][yaxis_column_name],
                text=dff[dff['country'] == i][text_column_name],
                mode='markers',
                opacity=0.7,
                marker={
                    'size': dff[dff['country'] == i][size_column_name],
                    'color': dff[dff['country'] == i][color_column_name],
                    'symbol': dff[dff['country'] == i][symbol_column_name],
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in dff[facet_column_name].unique()],





