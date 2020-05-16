import dash_html_components as html
import dash_trich_components as dtc


def Navbar():
    navbar = html.Div(
        [
            html.Div(
                [
                    html.Div(html.Div(
                        html.A(
                            'trich.ai', className="logo", href="https://trich.ai",
                        ))),
                    html.Div(
                        dtc.ThemeToggle()
                    ),

                ], className="container flex_row_btw"
            ),

        ],
        className="navbar"
    )
    return navbar
