# Data
import pandas as pd
import pickle

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State

from components.homepage import Homepage

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://fonts.googleapis.com/css2?family=Squada+One&display=swap']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = Homepage()


if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
