import dash_html_components as html
import dash_bootstrap_components as dbc


def Footer():
    footer = html.Div(
        html.Div(
            dbc.Row([
                dbc.Col('footer', width=6),
                dbc.Col('footer', width=6),
            ]),
            className="primary_bg radius8"),
        className="padding16")

    return footer
