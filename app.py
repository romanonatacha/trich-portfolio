# Data
import pandas as pd
import pickle

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

from components.homepage import Homepage


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])
app.layout = Homepage()

if __name__ == "__main__":
    app.run_server(debug=True)
