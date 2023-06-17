from dash import html
import dash_bootstrap_components as dbc
from components.card import Card
from data.portfolio_data import portfolio_data


def Portfolio():
    portfolio = html.Div(
        [
            dbc.Row(
                [
                    Card(
                        i["image"],
                        i["title"],
                        i["description"],
                        i["link"],
                        i["badge"],
                        i["git"],
                    )
                    for i in portfolio_data
                ],
                className="portfolio",
            )
        ]
    )
    return portfolio
