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
import datetime

import time
import random
from dash.dependencies import Input, Output
import datetime

  
# Generates a random number between
# a given positive range
app = dash.Dash(__name__)
cpu = []
memory = []
hard_disk = []
net_sent = []
net_recieve = []
gpu = []
t_end = time.time() +60*3
while time.time() < t_end:
    

    cpu_usage = psutil.cpu_percent()
    cpu.append(cpu_usage)
    memory_usage = psutil.virtual_memory().percent
    memory.append(memory_usage)
    disk_usage = psutil.disk_usage('D:\Silkbytes\phase_2').percent
    hard_disk.append(disk_usage)
    network_sent = psutil.net_io_counters().packets_sent
    net_sent.append(network_sent)
    network_recieved = psutil.net_io_counters().packets_recv
    net_recieve.append(network_recieved)
    Gpu_usage = GPUtil.getGPUs()
    gpu.append(Gpu_usage)



Prediction_data =({'Model Name': ['Human_Predicated', 'Model_Prediction'], 'Accuracy': [88,80]})  
df = pd.DataFrame(Prediction_data) 
fig = px.bar(df,x = 'Model Name',y = 'Accuracy', width = 400 , height = 400)
fig.show()






d_1 = {'cpu_usage':cpu}
df_1 = pd.DataFrame(d_1, columns=['cpu_usage'])

d_2 = {'memory_usage':memory}
df_2 = pd.DataFrame(d_2, columns=['memory_usage'])


d_3 = {'hard_disk_usage': hard_disk}
df_3 = pd.DataFrame(d_3, columns=['hard_disk_usage'])



d_4 = {'Packet_sent': net_sent, 'Packet_recieved':net_recieve }
df_4 = pd.DataFrame(d_4, columns=['Packet_sent','Packet_recieved'])


d_5 = {'Gpu_usage': gpu}
df_5 = pd.DataFrame(d_5, columns=['Gpu_usage'])



fig_1 = px.line(df_1,y = 'cpu_usage')
fig_1.update_layout(
    yaxis_range=[0, 100],       
)
fig_1.show()
fig_2 = px.line(df_2,y = 'memory_usage')
fig_2.update_layout(
    yaxis_range=[0, 100],       
)
fig_2.show()

fig_3 = px.line(df_3,y = 'hard_disk_usage')
fig_3.update_layout(
    yaxis_range=[0, 100],       
)
fig_3.show()


fig_4 = px.line(df_4)

fig_4.show()


fig_5 = px.line(df_5,y = 'Gpu_usage')
fig_5.update_layout(
    yaxis_range=[0, 100],       
)
fig_5.show()

app.layout = html.Div(children=[
        html.H1(children="Monitoring Dashboard", style={'text-align': 'center'}),

        html.Div(children='''
       This is a dashboard for showing HLP Accuraccy Vs. Model Accuraccy and also helping us montior Hardware Resources while Training deep learning model     
       '''),
       html.Div([
           html.Div([
            html.H3('HLP Vs. Model'),
            dcc.Graph(id='HlP-Graph', figure=fig)
        ], className="six columns"),
        html.Div([
            html.H3('CPU Usage'),
            dcc.Graph(id='cpu-graph', figure=fig_1)
        ], className="six columns"),

        html.Div([
            html.H3('Memory Usage'),
            dcc.Graph(id='Memory-graph', figure=fig_2)
        ], className="six columns"),
        
        html.Div([
            html.H3('Hard disk Usage'),
            dcc.Graph(id='Hard Disk-graph', figure=fig_3)
        ], className="six columns"),
    
       html.Div([
        html.H3('Netwok Usage'),
            dcc.Graph(id='Network-graph', figure=fig_4)
        ], className="six columns"),

       
        html.Div([
            html.H3('Gpu Usage'),
            dcc.Graph(id='Gpu-graph', figure=fig_5)
        ], className="six columns"),
        ], className="row"),
        
        
    
])


    

if __name__ == '__main__':
    app.run_server(debug=False)
   