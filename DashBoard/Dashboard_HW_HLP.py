# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 11:54:32 2021

@author: East Asia
"""

'''
import GPUtil
from threading import Thread
import time
import psutil

class Monitor(Thread):
    def __init__(self, delay):
        super(Monitor, self).__init__()
        self.stopped = False
        self.delay = delay # Time between calls to GPUtil
        self.start()

    def run(self):
        while not self.stopped:
            GPUtil.showUtilization()
           

            cpu_usage = psutil.cpu_percent()
 
            print(cpu_usage)

            memory_usage = psutil.virtual_memory()
            print(memory_usage)

            disk_usage = psutil.disk_usage('D:\Silkbytes\phase_2')
            print(disk_usage)

            network = psutil.net_io_counters()
            print(network)    
            time.sleep(self.delay)

    def stop(self):
        self.stopped = True
        
# Instantiate monitor with a 10-second delay between updates
monitor = Monitor(10)

# Train, etc.

# Close monitor
monitor.stop()
'''
'''
import threading
import psutil

def display_cpu():
    global running

    running = True

    currentProcess = psutil.Process()

    # start loop
    while running:
        print(currentProcess.cpu_percent(interval=1))

def start():
    global t

    # create thread and start it
    t = threading.Thread(target=display_cpu)
    t.start()

def stop():
    global running
    global t

    # use `running` to stop loop in thread so thread will end
    running = False

    # wait for thread's end
    t.join()
'''
import GPUtil
import dash
import psutil
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import time



app = dash.Dash(__name__)
memory = []
t_end = time.time() +1
while time.time() < t_end:
    

   
    memory_usage = psutil.virtual_memory().percent
    memory.append(memory_usage)
#mem_usage = psutil.virtual_memory().percent
    
d_2 = {'memory_usage':memory}
df1 = pd.DataFrame(
   
      d_2, columns=['memory_usage']
    )
second = len(df1)
df2 = pd.DataFrame(
    {
       " Time Elapsed (sec)": [second]
    })
print(df1)
print(df2)


result = pd.concat([df1, df2], axis=1, join='inner')
print(result)




fig = px.line(result, x='memory_usage', y=" Time Elapsed (sec)")
fig.update_layout(
    yaxis_range=[0, 101],
    xaxis_range=[0,60],
       
)



app.layout = html.Div(children=[
        html.H1(children='Hello Dash'),

        html.Div(children='''
       Dash: A web application framework for your data.
        '''),

        dcc.Graph(
        id='example-graph',
        figure=fig,
    
        
    ),
   dcc.Interval(
         id='interval-component',
         interval=1*1000, # in milliseconds
         n_intervals=0
        )
        ])
@app.callback(
 Output(component_id='example-graph', component_property='figure'),
 [Input(component_id='interval-component', component_property='n_intervals')]
) 

def remove_old_readings(df, rows_per_second=1):
    # remove old readings if they pass MONITOR_TIME
    seconds = []
    for sec in range(100):
        for _ in range(50):
            seconds.append(sec)


    return df


if __name__ == '__main__':
        app.run_server(debug=False)

