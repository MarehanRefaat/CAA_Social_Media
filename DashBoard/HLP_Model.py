# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 19:34:40 2021

@author: East Asia
"""

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.graph_objects as go
import plotly.express as px

app = dash.Dash(__name__)
import plotly.express as px

Prediction_data =({'Mdel Name': ['Human_Predicated', 'Model_Prediction'], 'Accuracy': [88,80]})  
df = pd.DataFrame(Prediction_data) 
fig = px.bar(df,x = 'Model Name',y = 'Accuracy', width=800, height=400)
fig.show()

app.layout = html.Div(children=[
    html.H1(children='Human Level Perfromance (HLP)'),

    html.Div(children='''
         Human Prediction Vs. Model Predicition.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=False)