import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from components.about import About
from components.stacks import Stacks
from components.portfolio import Portfolio

nav = Navbar()
about = About()
portfolio = Portfolio()
stacks = Stacks()

body = dbc.Container([
    about,
    stacks,
    portfolio
], className="top32 d_none", id="body_content")


def Homepage():
    layout = html.Div([
        nav,
        dbc.Spinner(id="loader"),
        body
    ])
    return layout
