import csv
import subprocess

import pandas            as pd
import numpy             as np
import seaborn           as sns
import plotly.express    as px
import matplotlib.pyplot as plt


from dash import Dash, html, dcc

app = Dash(__name__)
df_dash = pd.read_csv("data/processed/dados_processados.csv", sep = ",")

#/home/matheus/repos/covid19_leitos_go/data/processed/dados_processados.csv

app.layout = html.Div([
    html.Div(children = [
        html.Label('Tipo de Leito'),
        dcc.Dropdown(['Total', 'SUS', 'Não SUS'], 'Total'),

        html.Br()
        html.Label("Limpar filtros"),
        dcc.Dropdown([''])

    ])
])

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 8080, debug = True)