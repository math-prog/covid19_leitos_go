import dash

import pandas               as pd
import numpy                as np
import dash_core_components as dcc 
import dash_html_components as html

from   dash                 import Dash, html, dcc
from   dash.dependencies    import Input, Output, State


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
df_dash = pd.read_csv("data/processed/dados_processados.csv", sep = ",")

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
                    children="† Deaths are classified using the International Classification of Diseases, \
                    Tenth Revision (ICD–10). Drug-poisoning deaths are defined as having ICD–10 underlying \
                    cause-of-death codes X40–X44 (unintentional), X60–X64 (suicide), X85 (homicide), or Y10–Y14 \
                    (undetermined intent).",
                ),
            ],
        ),
])

if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port = 8080, debug = True)