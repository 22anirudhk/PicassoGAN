import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import numpy as np
import keras
from keras.models import load_model
from numpy.random import randn

import plotly.express as px

import time

layout = html.Div(children=[
    # Logo and About
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
                {'label': 'Romanticism', 'value': "Romanticism"},
                {'label': 'Neoclassical', 'value': "Neoclassical"},
                {'label': 'PicassoGAN Special', 'value': "fun"}
            ],
            value="Impressionism"
        ),

        html.H3("Click a style in the dropdown to generate new images.",
                id="tutorial-text"),


        # # Pictures
        # html.Div(children=[

        # ], id="picture-div"),

        dcc.Graph(
            id='graph'
        ),

    ], id="content-div")
], className="everything")


@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('style-dropdown', 'value')])
def update_images(value):
    import os

    print("EEEEEEEEEEEEEEEEE" + value)

    # generate points in latent space as input for the generator
    def generate_latent_points(latent_dim, n_samples):
        # generate points in the latent space
        x_input = randn(latent_dim * n_samples)
        # reshape into a batch of inputs for the network
        x_input = x_input.reshape(n_samples, latent_dim)
        return x_input

    # load model
    filepath = 'models/' + value.lower() + '_model.h5'

    print("ABOVEABOVEABOVE")
    model = keras.models.load_model(str(filepath))
    print("BELOWBELOWBELOW")

    # generate images
    latent_points = generate_latent_points(100, 9)
    print("LATENT_POINTS")
    # generate images
    X = model.predict(latent_points)
    print("PREDICT")
    # scale from [-1,1] to [0,1]
    X = (X + 1) / 2.0

    from plotly.subplots import make_subplots
    import plotly.graph_objects as go

    fig = make_subplots(rows=3, cols=3)

    row = 1
    col = 1
    for img_arr in X:
        if(col == 4):
            row += 1
            col = 1
        img_arr = img_arr * 255
        # img_arr = img_arr.astype(np.uint8)
        fig.add_trace(px.imshow(img_arr).data[0], row=row, col=col)
        col += 1
    # fig.show()
    fig.update_layout(height=800, width=800)

    fig.print_grid()

    fig.update_yaxes(visible=False, showticklabels=False)
    fig.update_xaxes(visible=False, showticklabels=False)

    return fig

    # # Save images to pictures directory
    # from PIL import Image

    # index = 1
    # for img_arr in X:
    #     img_arr = img_arr * 255
    #     img_arr = img_arr.astype(np.uint8)
    #     img = Image.fromarray(img_arr)
    #     img_path = 'assets/pictures/image-' + str(index) + '.jpeg'

    #     print(img_path)

    #     img.save(img_path)
    #     index += 1
    # add_images()

    # Generate the images based on the style and then return them into pictureDiv
    # if(value == "Impressionism"):
    # return [
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-1.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-2.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-3.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-4.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-5.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-6.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-7.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-8.jpeg"), className="picture"),
    #     html.Img(src=app.get_asset_url(
    #         "pictures/image-9.jpeg"), className="picture")
    # ]
