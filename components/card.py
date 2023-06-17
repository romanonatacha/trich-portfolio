import dash_bootstrap_components as dbc

from dash import html


def Card(image, title, description, link, badge, git):

    card = dbc.Col(
        html.Div(
            [
                html.A(
                    html.Div(
                        html.Img(src=image, alt=title),
                        className="bottom16 portfolio_card_img",
                    ),
                    href=link,
                    target="_blank",
                ),
                html.Div(
                    [
                        html.H4(title, className="font-sm bold uppercase"),
                        html.P(description, className="font-xs bottom8"),
                    ],
                    className="portfolio_card_text bottom16",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    dbc.Badge(
                                        i,
                                        className="mr-1 self_center default_inverse primary_bg",
                                    ),
                                    className="inline-block",
                                )
                                for i in badge
                            ]
                        ),
                        html.A(
                            html.I(className="fab fa-github font-sm terciary"),
                            href=git,
                            target="_blank",
                        ),
                    ],
                    className="font-xs flex_row_btw portfolio_card_footer",
                ),
            ],
            className="second_bg padding16 radius8 portfolio_card",
        ),
        className="padding16",
        lg=3,
        md=4,
        sm=6,
        xs=12,
    )
    return card
