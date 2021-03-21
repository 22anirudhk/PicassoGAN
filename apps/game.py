import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import random

from app import app


# def add_images():


# images = add_images()
# a = images[0]
# b = images[1]
# c = images[2]

score = 0
ans = -1

layout = html.Div(children=[
    dcc.Store(id='local', storage_type='local'),

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

    html.H4("Task: find which of the images is fake by clicking on the corresponding button. Press any button to start."),


    html.Div(children=[
        html.H3("Score: "),
        html.H3("", id="score")
    ], id="score-div"),


    html.Div(children=[
        html.Div(children=[

        ], id="game-image-div")
    ], id="game-div"),
    html.Div(children=[
        html.Button('1', id='btn-1', className="btn"),
        html.Button('2', id='btn-2', className="btn"),
        html.Button('3', id='btn-3', className="btn"),
    ], id="button-div"),

    html.Div("", id="ans"),
], className="everything")


# When a button is clicked, it sees if the player chose the right answer. If it did, it increases the score.
@app.callback([Output("local", 'data'), Output('game-image-div', 'children')],
              [Input('btn-1', 'n_clicks'),
               Input('btn-2', 'n_clicks'),
               Input('btn-3', 'n_clicks')],
              [State("local", 'data')])
def displayClick(btn1, btn2, btn3, data):
    # Give a default data dict with 0 clicks if there's no data.
    data = data or {'ans': -1, "score": 0}

    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    button_clicked = -1
    if 'btn-1' in changed_id:
        button_clicked = 1
    elif 'btn-2' in changed_id:
        button_clicked = 2
    elif 'btn-3' in changed_id:
        button_clicked = 3

    ans = int(data['ans'])
    if(ans == button_clicked):
        # print("in")
        data['score'] = int(data['score']) + 1

    # put new images
    # Pick 3 random real images
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    while(b == a):
        random.randint(1, 9)

    c = random.randint(1, 9)
    while(c == b or c == a):
        random.randint(1, 9)

    # modify the path later for real images
    a_path = "pictures/monet-" + str(a) + ".png"
    b_path = "pictures/monet-" + str(b) + ".png"
    c_path = "pictures/monet-" + str(c) + ".png"

    # store correct answer
    data['ans'] = 3

    imgs = [html.Img(src=app.get_asset_url(
            a_path), className="picture"),
            html.Img(src=app.get_asset_url(
                b_path), className="picture"),
            html.Img(src=app.get_asset_url(
                c_path), className="picture")]

    # print(imgs)

    return data, imgs


# outputs both the score and the current answer
# code snippet modified from Dash documentation
@app.callback([Output('score', 'children'), Output('ans', 'children')],
              # Since we use the data prop in an output,
              # we cannot get the initial data on load with the data prop.
              # To counter this, you can use the modified_timestamp
              # as Input and the data as State.
              # This limitation is due to the initial None callbacks
              # https://github.com/plotly/dash-renderer/pull/81
              [Input('local', 'modified_timestamp')],
              [State('local', 'data')])
def on_data(ts, data):
    return data.get('score', 0), data.get('ans', 0)
