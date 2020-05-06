import dash_bootstrap_components as dbc
import dash_core_components as dcc

import dash_html_components as html


def Navbar():
    navbar = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(html.Div(
                        html.A(
                            'trich.ai', className="logo", href="https://trich.ai",
                        )), width=10),
                    dbc.Col([
                        html.Div(
                            [
                                dbc.Checkbox(
                                    id="theme_selector", className="container_toogle"),
                                dbc.Label(
                                    html_for="theme_selector",
                                    className="form-check-label"
                                ),
                            ], id="toggle_theme"
                        ),
                        dbc.Tooltip(
                            "Toggle light/dark theme",
                            target="toggle_theme",
                            delay=1000
                        ),
                    ], width=2)
                ], className="total_width"
            )
        ],
        className="navbar"
    )
    return navbar
