import dash_bootstrap_components as dbc
import dash_html_components as html


def Card(image, title, description, link):
    card = html.Div([
        html.Div(
            html.Img(src=image, alt=title)),
        html.Div([
            html.H4(title, className="font-sm"),
            html.P(description, className="font-xs"),
            html.Div([
                html.A('open project', href=link, target="_blank"),
                html.A('git', href=link, target="_blank"),
            ], className="font-xs")
        ])
    ], className="portfolio_card padding16")
    return card
