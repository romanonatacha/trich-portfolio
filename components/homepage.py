import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from components.navbar import Navbar
from components.about import About
from components.stacks import Stacks
from components.portfolio import Portfolio
from components.footer import Footer

nav = Navbar()
about = About()
portfolio = Portfolio()
stacks = Stacks()
footer = Footer()

body = dbc.Container([about, stacks, portfolio, footer], className="top32")


def Homepage():
    layout = html.Div([nav, body], id="homepage")
    return layout
