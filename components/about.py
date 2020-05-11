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
                        html.Div(
                            "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.",
                            className="font-sm",
                        ),
                        html.Div(className="bottom32 dt_hide"),
                    ], lg=9, sm=12),
                    dbc.Col([
                        dbc.Row([
                            dbc.Col("Total", width=12,
                                    className="bold uppercase"),
                            dbc.Col([
                                html.I(className="fab fa-github padding8"),
                                html.Span("+"),
                                html.I(className="fab fa-kaggle padding8")
                            ], width=12, className="font-lg padding16"),
                            dbc.Col(['Followers ',
                                     html.Br(className="dt_hide"),
                                     html.Span('3000', className="bold font-md")], lg=12, sm=4),
                            dbc.Col(['Forks ',
                                     html.Br(className="dt_hide"),
                                     html.Span(
                                         '378', className="bold font-md")], lg=12, sm=4),
                            dbc.Col(['Stars/Votes ',
                                     html.Br(className="dt_hide"),
                                     html.Span('7089', className="bold font-md")], lg=12, sm=4)
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
                        ], className="about_logos font-xl"),
                        width=12
                    )

                )
            ], className="about_content padding32")
        ], className="terciary_bg radius8 relative about")
    ], className="padding16")
    return about
