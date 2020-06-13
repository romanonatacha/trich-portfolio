import dash_html_components as html
import dash_bootstrap_components as dbc


def About():
    about = html.Div([
        html.Div([
            html.H4(
                "ABOUT",
                className="font-xl bold letter_spac8 default_inverse"
            ),
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            "trich.ai is a company founded by the Data Scientist and Kaggle Grandmaster, Leonardo Ferreira vising to build an interdisciplinary company to do consulting, build data web apps to clients, and launch own products;\
                                On trich.ai we have already built solutions for some of the biggest companies around the world, building creative and profitable results to our clients. We mainly focus on open-source solutions.", html.Br(), html.Br(),
                            "Visit our GitHub to get the code of all platforms, we believe that together, we can go furthest."],
                            className="font-sm",
                        ),
                        html.Div(className="bottom32 dt_hide"),
                    ], lg=9, sm=12),
                    dbc.Col([
                        dbc.Row([
                            dbc.Col([
                                html.I(className="fab fa-github padding16"),
                                html.Span("+"),
                                html.I(className="fab fa-kaggle padding16")
                            ], width=12, className="font-lg"),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col('Followers', lg=6),
                                    dbc.Col(
                                        '2k+', className="bold font-md", lg=6),
                                ]),
                            ], lg=12, width=4),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col('Stars/Votes ', lg=6),
                                    dbc.Col(
                                        '5k+', className="bold font-md", lg=6),
                                ]),
                            ], lg=12, width=4),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col('Forks', lg=6),
                                    dbc.Col(
                                        '6k+', className="bold font-md", lg=6),
                                ]),
                            ], lg=12, width=4),
                        ], className="text-center")
                    ], className="git_kag", lg=3, sm=12)
                ]),
                dbc.Row(
                    dbc.Col(
                        html.Div([
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-linkedin-in"),
                                    href="https://www.linkedin.com/company/trich-ai/",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-kaggle"),
                                    href="https://www.kaggle.com/kabure/notebooks",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-github "),
                                    href="https://github.com/kaburelabs",
                                    target="_blank"
                                )
                            ),
                            html.Div(
                                html.A(
                                    html.I(className="fab fa-medium-m"),
                                    href="https://medium.com/@kabure",
                                    target="_blank"
                                )
                            )
                        ], className="about_logos font-lg"),
                        width=12
                    )

                )
            ], className="about_content padding32")
        ], className="terciary_bg radius8 relative about")
    ], className="padding16")
    return about
