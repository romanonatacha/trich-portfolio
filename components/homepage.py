import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from components.navbar import Navbar
from data.portfolio_data import portfolio_data

nav = Navbar()

body = dbc.Container(

)


def Homepage():
    layout = html.Div([
        nav,
        body,
        html.Ul([
            html.Li([
                html.P(i['title']),
                html.P(i['desc'])
            ]) for i in portfolio_data
        ])
    ])
    return layout
