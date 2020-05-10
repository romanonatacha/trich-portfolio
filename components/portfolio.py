import dash_html_components as html
from components.card import Card
from data.portfolio_data import portfolio_data


def Portfolio():
    portfolio = html.Div([
        html.Div([
            Card(i['image'], i['title'], i['description'], i['link'], i['badge']) for i in portfolio_data
        ], className="portfolio desktop"),
        html.Div([
            Card(i['image'], i['title'], i['description'], i['link'], i['badge']) for i in portfolio_data
        ], className="portfolio mobile")
    ])
    return portfolio
