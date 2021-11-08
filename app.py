import json
from flask import Flask, render_template, request
from backend.Grid import Grid, UP, DOWN, LEFT, RIGHT
from backend.Game import Game

app = Flask('__name__')

TIME_LIMIT = 0.6  # How much time does AI-player have pr move?
DIR_DICT = {"u": UP, "d": DOWN, "l": LEFT, "r": RIGHT}
DIR_TO_ARROW = {1: "&uarr;", 2: "&darr;", 3: "&larr;", 4: "&rarr;"}


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/new_game", methods=['GET'])
def new_game():
    data = {"grid": Grid(4, 4)._map}
    # data = {"grid": [[11, 4, 8, 16], [32, 64, 128, 512], [1024, 2048, 4096, 8], [7, 2048, 4096, 3]]}
    return data


@app.route("/ai_move", methods=['POST'])
def ai_move():
    grid = Grid(4, 4)
    grid._map = json.loads(request.form['grid'])
    game = Game(grid, time_limit=TIME_LIMIT)
    direction, info = game.make_ai_move()
    data = {"grid": game.grid._map}
    if game.game_over:
        data["game_over"] = True
    else:
        data["direction"] = DIR_TO_ARROW[direction]
    return data


@app.route("/human_move", methods=['POST'])
def human_move():
    direction = DIR_DICT[request.form['direction']]
    grid = Grid(4, 4)
    grid._map = json.loads(request.form['grid'])
    game = Game(grid, time_limit=TIME_LIMIT)
    game.make_human_move(direction)
    data = {"grid": game.grid._map, "direction": DIR_TO_ARROW[direction]}
    if game.game_over:
        data["game_over"] = True
    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
