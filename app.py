# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    #Logo and About
    html.Div(children=[
        html.Div(children=[
            html.H1("PicassoGAN", id="title"),
            html.H3("MACHINE GENERATED ART", id="subtitle")
        ], id="logo-div"),
        html.H3("ABOUT", id="about")
    ], id="header-div"),
    html.Div(children=[
        # Pictures
        html.Div(children=[

        ], id="picture-div"),
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

    ], id="content-div")
], id="everything")


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


if __name__ == '__main__':
    app.run_server(debug=True)
