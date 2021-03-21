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
        html.H3("What does this project do?"),
        html.P("Everytime you choose a different art style, a machine learning model generates completely new paintings. The model used is a GAN (Generative Adversarial Network).", className="about-answers"),

        html.H3("How do GANs work?"),
        html.P("There are two networks competing against each other. One tries to detect fake images, and one tries to generate them. As they are fed in data (here real paintings), the generator becomes better at generating paintings and the discriminator becommes better at detecting fake ones. They both improve each other.", className="about-answers"),

        html.H3("How did you make it?"),
        html.P("We compiled thousands of training images for each art style, then made them into the same format so the network could read them, trained the models, and then deployed the models to the website which you are viewing right now.", className="about-answers"),

    ], id="about-content")
], className="everything")
