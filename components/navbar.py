import dash_bootstrap_components as dbc
import dash_html_components as html


def Navbar():
    navbar = dbc.Navbar(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Div('trich.ai', className="logo")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://trich.ai",
            )
        ],
        color="dark",
        dark=True,
    )
    return navbar
