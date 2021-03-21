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
    html.Div(children=[
        # Selector for art type
        dcc.Dropdown(
            id='style-dropdown',
            options=[
                {'label': 'Impressionism', 'value': "Impressionism"},
                {'label': 'Post-Impressionism', 'value': "Post-Impressionism"},
                {'label': 'Realism', 'value': "Realism"},
                {'label': 'Romanticism', 'value': "Romanticism"}
            ],
            value="Impressionism"
        ),

        # Pictures
        html.Div(children=[

        ], id="picture-div"),


    ], id="content-div")
], className="everything")


@app.callback(
    dash.dependencies.Output('picture-div', 'children'),
    [dash.dependencies.Input('style-dropdown', 'value')])
def update_images(value):
    # Generate the images based on the style and then return them into pictureDiv
    # if(value == "Impressionism"):
    return [
        html.Img(src=app.get_asset_url(
            "pictures/monet-1.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-2.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-3.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-4.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-5.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-6.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-7.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-8.png"), className="picture"),
        html.Img(src=app.get_asset_url(
            "pictures/monet-9.png"), className="picture")
    ]
