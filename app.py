# Data
import pandas as pd

# Dash
import dash
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
from components.homepage import Homepage

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.css',
    'https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;700&display=swap',
    'https://fonts.googleapis.com/css2?family=Squada+One&display=swap',
    'https://use.fontawesome.com/releases/v5.8.1/css/all.css']

external_scripts = [
    'https://code.jquery.com/jquery-3.5.1.min.js',
    'https://cdn.jsdelivr.net/npm/slick-carousel@1.8.1/slick/slick.min.js'
]

meta_tags = [
    {
        "name": "viewport",
        "content": "width=device-width, initial-scale=1, maximum-scale=1",
    },
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    meta_tags=meta_tags
)

app.title = "trich.ai portfolio"


app.index_string = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
      
        <div class="sharethis-inline-reaction-buttons"></div>
        <script type='text/javascript' src='https://platform-api.sharethis.com/js/sharethis.js#property=5e9606b2a034e50012b52e4a&product=sop' async='async'></script>
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-1DYNFQVF7N"></script>
        <script data-name="BMC-Widget" src="https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js" data-id="shfZKbL" data-description="Help to keep building web apps for free;" data-message="Thank you for visiting. You can support the projects here." data-color="#FF813F" data-position="" data-x_margin="50" data-y_margin="18"></script>
        </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>"""


server = app.server

app.layout = Homepage()


if __name__ == "__main__":
    app.run_server(debug=True)
