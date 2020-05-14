# Data
import pandas as pd

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
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

meta_tags = [
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, maximum-scale=1",
    },
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    meta_tags=meta_tags
)

server = app.server

app.layout = Homepage()


@app.callback(
    Output("homepage", "data-theme"),
    [
        Input("theme_selector", "checked"),
    ],
)
def on_form_change(checkbox_checked):
    if checkbox_checked:
        return "dark"
    else:
        return "light"


if __name__ == "__main__":
    app.run_server(debug=True)
