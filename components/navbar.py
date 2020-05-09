import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def Navbar():
    navbar = html.Div(
        [
            html.Div(
                [
                    html.Div(html.Div(
                        html.A(
                            'trich.ai', className="logo", href="https://trich.ai",
                        ))),
                    html.Div([
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
                            delay={'show': 1000}
                        ),
                    ])
                ], className="boxed flex_row_btw"
            )
        ],
        className="navbar"
    )
    return navbar
