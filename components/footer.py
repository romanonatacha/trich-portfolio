import dash_html_components as html
import dash_bootstrap_components as dbc


def Footer():
    footer = html.Div(
        html.Div(
            dbc.Row([
                dbc.Col([
                    html.Div(
                        'Contact', className="uppercase bold font-xs padding4"),
                    html.Div(
                        html.A(
                            'contact@trich.ai',
                            href="mailto:contact@trich.ai",
                            target="_blank"
                        ), className="padding4"),
                ], lg=8, width=12),
                dbc.Col([
                    html.Div([
                        html.Ul([
                            html.Li(
                                html.A([
                                    html.I(className="fab fa-slack mr-1"),
                                    html.Span(' dash learners community'),
                                ], target="_blank", href="https://join.slack.com/t/dash-learners/shared_invite/zt-edu12c6t-SNk5owutigiqS4mwkmC75A"),
                                className="padding4"
                            ),
                            html.Li(
                                html.A([
                                    html.I(className="fab fa-python mr-1"),
                                    html.Span(
                                        ' dash trich components library'),
                                ], target="_blank", href="https://pypi.org/project/dash-trich-components/"),
                                className="padding4"
                            )
                        ])
                    ])
                ], lg=4, width=12),
            ], className="padding32"),
            className="primary_bg radius8"),
        className="padding16 default_inverse footer font-sm")

    return footer
