# Data
import pandas as pd

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from components.homepage import Homepage


external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css',
    'https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap',
    'https://fonts.googleapis.com/css2?family=Squada+One&display=swap',
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css']

external_scripts = [
    'https://code.jquery.com/jquery-3.5.1.min.js',
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js'
]


app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)

server = app.server

app.layout = Homepage()


if __name__ == "__main__":
    app.run_server(debug=True)
