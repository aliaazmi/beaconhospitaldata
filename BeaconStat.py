#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
import plotly.express as px
import plotly.io as pio
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output
from dash import Dash, dash_table


# In[3]:


df = pd.read_csv('https://raw.githubusercontent.com/aliaazmi/dataalia/main/Data_base_cancer_4_1.csv')
df.head()


# In[ ]:


app = Dash(__name__)

columns = [
    dict(id='Year', name='Year'),
    dict(id='amount', name='Pt Amount', type='numeric'),
]

data = [
    dict(Year='2019', amount=2461),
    dict(Year='2020', amount=2439),
    dict(Year='2021', amount=2015),
    dict(Year='2022-until July', amount=1200)
]
app.title = 'Beacon Hospital Cancer Pt Statistic 2019-2022'

app.layout = html.Div([
    html.H1('Beacon Hospital Cancer Pt Statistic 2019-2022'),
    
    
    html.H3('Filter The Year'),
    dcc.Dropdown(id='year-choice',
                 options=[{'label':x,'value':x}
                            for x in sorted (df.Year.unique())],
                            value='2019', style={'width':'50%'}),
    html.H6(''),
    html.H6(''),
    dash_table.DataTable( id= 'table',  data=data, columns=columns,
        style_cell_conditional=[
        { 'textAlign': 'center'
        }
    ],
       style_header={
        'backgroundColor': 'rgb(50, 50, 50)',
        'fontWeight': 'bold',
        'color': 'white'
    },
    style_data={
        'backgroundColor': 'white',
        'fontWeight': 'bold'

    }, 
                         
),
    
    dcc.Graph(id='my-graph'),
])


@app.callback(
    Output(component_id="my-graph", component_property="figure"), 
    Input(component_id="year-choice", component_property="value"),
    
)
    
def interactive_graphing(value_year):
    dff = df[df.Year==value_year]
    fig = px.pie(dff, values='Count', names='Cancer',
             title='Beacon Hospital Cancer Pt Statistic',
             labels ='Cancer')
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig


if __name__=='__main__':  
    app.run_server()


# In[ ]:




