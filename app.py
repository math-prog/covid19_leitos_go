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


from dash           import Dash, html, dcc
from urllib.request import urlopen


# Initialize App

app = dash.Dash(
    __name__,
    meta_tags= [
        {"name": "viewport", "content": "width = device-width, initial-scale= 1.0"}
     ],
)

app.title = "Unidades Hospitalares do Estado de Goiás ( COVID-19 )"
server = app.server

# Load data
df = pd.read_csv("data/processed/dados_processados.csv", sep = ",", index_col = 0)

#load geojson
with urlopen('https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-52-mun.json') as data:
    geojson_goias = json.load(data)


YEARS = [2019, 2020, 2021, 2022]

DEFAULT_COLORSCALE = [
    "#f2fffb",
    "#bbffeb",
    "#98ffe0",
    "#79ffd6",
    "#6df0c8",
    "#69e7c0",
    "#59dab2",
    "#45d0a5",
    "#31c194",
    "#2bb489",
    "#25a27b",
    "#1e906d",
    "#188463",
    "#157658",
    "#11684d",
    "#10523e",
]

# App layout

app.layout = html.Div(
      id="root",
    children=[
        html.Div(
            id="header",
            children=[
                html.A(
                    html.Button("Source Code", className="link-button"),
                    href="https://github.com/math-prog/covid19_leitos_go",
                ),
                html.H4(children="Acompanhamento dos leitos hospitalares do Estado de Goiás"),
                html.P(
                    id="description",
                    children="Os dados foram obtidos pelo site DATASUS, através da biblioteca R microdatasus [1], analisando os leitos hospitalares no Estado de Goiás dos anos de 2019 a 2022.\
                    [1] SALDANHA, Raphael de Freitas; BASTOS, Ronaldo Rocha; BARCELLOS, Christovam. Microdatasus: pacote para download e pré-processamento de microdados do\
                         Departamento de Informática do SUS (DATASUS). Cad. Saúde Pública, Rio de Janeiro , v. 35, n. 9, e00032419, 2019 . Available from http://ref.scielo.org/dhcq3y.",
                ),
            ],
        ),
        html.Div(
            id = "app-Container",
            children=[
                html.Div(
                    id = "left-column",
                    children=[
                        html.Div(
                            id = "slider-text",
                            children = "Drag the slider to change the year:",
                        ),
                        dcc.Slider(
                            id = "years-slider",
                            min = df['ANO'].min(),
                            max = df['ANO'].max(),
                            value = df['ANO'].min(),
                            marks = {
                                str(year): {
                                    "label": str(year),
                                    "style": {"color": "#7fafdf"},
                                }
                                for year in df['ANO']
                            },
                        ),
                    ],
                ),
                html.Div(
                    id = "heatmap-container",
                    children = [
                        html.P( "Mapa de distriuição dos leitos hospitalares no Estado de Goias",
                        id = "heatmap-title",

                        ),
                    
                        dcc.Graph(
                            id = "county-choropleth",

                        )

                    ]
                )
            ],
        ),
       
])

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 8080, debug = True)