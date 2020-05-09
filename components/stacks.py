import dash_html_components as html
from data.stacks_data import stacks_data


def Stacks():
    stacks = html.Div([
        html.Button(
            html.I(className="fas fa-angle-left secondary font-xl"),
            className="prev absolute btn",
            style={'top': '35%', 'left': '-30px'}
        ),
        html.Button(
            html.I(className="fas fa-angle-right  secondary font-xl"),
            className="next absolute btn",
            style={'top': '35%', 'right': '-30px'}
        ),
        html.Div([
            html.Div(
                html.Img(alt=i['name'], src=i['image']),
                className="item padding16 margin16 radius8 white_bg"
            ) for i in stacks_data
        ], className="stacks padding16")
    ], className="relative stacks_container")

    return stacks
