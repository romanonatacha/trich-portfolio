import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from components.card import Card

from data.portfolio_data import portfolio_data

nav = Navbar()

body = dbc.Container([
    html.Div([
        Card(i['image'], i['title'], i['description'], i['link']) for i in portfolio_data
    ], className="portfolio")
])


def Homepage():
    layout = html.Div([
        nav,
        body
    ])
    return layout
