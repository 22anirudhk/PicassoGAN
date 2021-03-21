import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
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

    html.Div(children=[
        html.H4("You have to find which of the images is real by clicking on the corresponding button. Press any button to start."),

        html.H3("", id="score"),

        html.Button('1', id='btn-1'),
        html.Button('2', id='btn-2'),
        html.Button('3', id='btn-3'),

        html.Div(children=[

        ], id="game-image-div")
    ], id="game-div")
], className="everything")


# add a click to the appropriate store.
@app.callback(Output(store, 'data'),
              Input('btn-1', 'id'),
              Input('btn-2', 'id'),
              Input('btn-3', 'id'),
              State(store, 'data'))
def displayClick(btn1, btn2, btn3, data):
    # Give a default data dict with 0 clicks if there's no data.
    data = data or {'clicks': 0}

    data['clicks'] = data['clicks'] + 1
    return data

    # output the stored clicks in the table cell.
    @app.callback(Output('{}-clicks'.format(store), 'children'),
                  # Since we use the data prop in an output,
                  # we cannot get the initial data on load with the data prop.
                  # To counter this, you can use the modified_timestamp
                  # as Input and the data as State.
                  # This limitation is due to the initial None callbacks
                  # https://github.com/plotly/dash-renderer/pull/81
                  Input(store, 'modified_timestamp'),
                  State(store, 'data'))
    def on_data(ts, data):
        if ts is None:
            raise PreventUpdate

        data = data or {}

        return data.get('clicks', 0)


@app.callback([Output('game-image-div', 'children'),
               Output('score', 'children')],
              [Input('btn-1', 'n_clicks'),
               Input('btn-2', 'n_clicks'),
               Input('btn-3', 'n_clicks')])
def displayClick(btn1, btn2, btn3):
    # if(ans > 0):
    #     # See which button was pressed and update their score
    #     changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    #     button_clicked = -1
    #     if 'btn-1' in changed_id:
    #         button_clicked = 1
    #     elif 'btn-2' in changed_id:
    #         button_clicked = 2
    #     elif 'btn-3' in changed_id:
    #         button_clicked = 3
    #     if(button_clicked == ans):
    #         ans += 1

    # See which button was pressed and update their score
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    button_clicked = -1
    if 'btn-1' in changed_id:
        button_clicked = 1
    elif 'btn-2' in changed_id:
        button_clicked = 2
    elif 'btn-3' in changed_id:
        button_clicked = 3

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

    # also generate random image

    # update current answer
    ans = 3

    return [
        html.Img(src=app.get_asset_url(
            a_path), className="picture"),
        html.Img(src=app.get_asset_url(
            b_path), className="picture"),
        html.Img(src=app.get_asset_url(
            c_path), className="picture"),
    ], score
