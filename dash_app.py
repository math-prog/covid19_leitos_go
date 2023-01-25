import csv
import dash
import json
import subprocess

import pandas               as pd
import numpy                as np
import seaborn              as sns
import plotly.express       as px
import matplotlib.pyplot    as plt
import plotly.graph_objects as go 
import plotly.offline       as pyo


from dash           import Dash, html, dcc, Input, Output
from urllib.request import urlopen


# Initialize App

app = Dash(__name__)

app.title = "Unidades Hospitalares do Estado de Goiás ( COVID-19 )"

# Load data
df = pd.read_csv("data/processed/dados_processados.csv", sep = ",", index_col = 0, low_memory = False)

#load geojson
with urlopen('https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-52-mun.json') as data:
    geojson_goias = json.load(data)

# App Layout 

app.layout = html.Div([
    
    html.Div([

        html.Div([
            html.Br(),
            html.Label("Selecione o ano:"),
            dcc.Dropdown(
                df['ANO'].unique(),
                '2019',
                #multi = True,
                id = 'year-selection'
            ),
        ], style = {'width': '50%', 'float': 'left','display': 'inline-block'}),
    
   ]),

    html.Div([
        html.Br(),
        html.Label("Selecione o tipo de Leito"),
        html.Div([
            dcc.Checklist(["Leitos Totais", "Nao SUS", "SUS"],
            id = 'bed-type',
            ),
        ]),
    ], style = {'width': '40%', 'float': 'right', 'display': 'inline-block'}),

   html.Div([
            dcc.Graph(
            id = 'goias-map',
            ), 
   ], style = {'display': 'inline-block', 'width': '60%', 'float': 'left',}),
])


@app.callback(
    Output('goias-map', 'figure'),
    Input('year-selection','value'))

def upgrade_graph(year_selection):

    aux1 = df[df['ANO'] == year_selection]

    fig = px.choropleth_mapbox(aux1,
                                locations = 'CIDADE',
                                geojson = geojson_goias,
                                featureidkey = 'properties.name',
                                color = 'QT_EXIST',
                                hover_name = 'CIDADE',
                                hover_data = ['QT_EXIST', 'LATITUDE', 'LONGITUDE'],
                                color_continuous_scale = "Viridis",
                                mapbox_style = "carto-positron",
                                center = {'lat': -16.65, 'lon' : -49.49},
                                zoom = 3,
                                opacity = 0.5,
                            )


    return fig

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 8080, debug = True)

