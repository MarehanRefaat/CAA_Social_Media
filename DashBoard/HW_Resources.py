# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 09:21:43 2021

@author: East Asia
"""



import psutil
import GPUtil
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
#while(1):

cpu_usage = psutil.cpu_percent()
 
print(cpu_usage)

memory_usage = psutil.virtual_memory()
print(memory_usage)



disk_usage_d = psutil.disk_usage('D:\')
print(disk_usage_d)

network = psutil.net_io_counters()
print(network)



GPUtil.showUtilization()


app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "cpu_usage": [cpu_usage],
    "memory_usage": [memory_usage],
    "disk_usage": [disk_usage],
    "network": [network],
    " GPU": [GPUtil.showUtilization()]
    
})

fig = px.pie(df)

app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
        Dash: A web application framework for your data.
        '''),

        dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)