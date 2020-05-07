import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from components.about import About
from components.card import Card

from data.portfolio_data import portfolio_data

nav = Navbar()
about = About()

body = dbc.Container([
    about,
    html.Div([
        Card(i['image'], i['title'], i['description'], i['link'], i['tech']) for i in portfolio_data
    ], className="portfolio")
], className="top32")


def Homepage():
    layout = html.Div([
        nav,
        body
    ])
    return layout
