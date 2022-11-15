import dash
from dash.dependencies import Input, Output, State
from dash import dcc
from dash import html
import plotly.express as px

import pandas as pd
#data
df = pd.read_csv("WhatsgoodlyData-10.csv")
df_subset = pd.read_csv("subset.csv")
df2 = df[df['Segment Type'] == 'University']

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)
app.layout = html.Div([
    html.H1("WhatsgoodlyData Statistics", style={"textAlign":"center"}),
    html.Hr(),
    html.H3("Which application is checked first after notification on phone?", style={"textAlign":"center"}),
    html.Div([
        dcc.Graph(id='mob+web', figure=px.pie(data_frame=df[0:8], names='Answer', values='Percentage', title='Total Responses'), className='three columns'),
        dcc.Graph(id='gender', figure=px.histogram(df[8:16], x='Answer', y='Percentage', color='Segment Description', barmode='group', title="Difference Between Female and Male Responses"), className='five columns'),
        dcc.Graph(id='mobile', figure=px.pie(data_frame=df[:4], names='Answer', values='Percentage', title='Mobile Responses'), className='three columns'),
        ]),
    html.Div([
        dcc.Graph(id='five', figure=px.pie(data_frame=df[416:420], names='Answer', values='Percentage', title="Collage Students' Responses"), className='three columns'),
        dcc.Graph(id='four', figure=px.histogram(df_subset, x='Answer', y='Count', color='Segment Description', barmode='group'), className='five columns'),
        dcc.Graph(id='six', figure=px.pie(data_frame=df2, names='Answer', values='Percentage', title="University Students' Responses"), className='three columns'),
        ])
    ])
if __name__ == '__main__':
    app.run_server(debug=True)