import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div(children=[
    #Logo and About
    html.Div(children=[
        html.Div(children=[
            html.A("PicassoGAN", className="title", href="/"),
            html.H3("MACHINE GENERATED ART", className="subtitle")
        ], className="logo-div"),
        html.Div(children=[
            html.A("GAME", className="game", href="/game"),
            html.A("ABOUT", className="about", href="/about")
        ], className="top-right-div")
    ], className="header-div"),
], className="everything")
