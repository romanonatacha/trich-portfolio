from dash import html
import dash_trich_components as dtc
from data.stacks_data import stacks_data


def Stacks():
    stacks = html.Div(
        [
            dtc.Carousel(
                [
                    html.Div(
                        html.Img(alt=i["name"], src=i["image"]),
                        className="item padding16 margin16 radius8 white_bg",
                    )
                    for i in stacks_data
                ],
                slides_to_scroll=1,
                swipe_to_slide=True,
                autoplay=True,
                speed=2000,
                variable_width=True,
                center_mode=True,
                responsive=[{"breakpoint": 991, "settings": {"arrows": False}}],
            )
        ],
        className="stacks padding16",
    )

    return stacks
