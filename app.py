  
# Setup instuctions for Flask in Visual Studio Code
# 1) Open folder with flask project
# 2) In terminal: "pip install flask" (if necessary)
# 3) In terminal: "python app.py"

import json
from flask import Flask, render_template, request
from backend.Grid import Grid, UP, DOWN, LEFT, RIGHT
from backend.Game import Game

app = Flask('__name__')

TIME_LIMIT = 0.6 # How much time does AI-player have pr move?


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        action = "new_game"
   
    else: 
        data = json.loads(request.form["json_data"])   #return(json.dumps(data))
        action = data["requested_action"]

    if action == 'new_game': 
        grid = Grid(4,4)
        #grid._map = [[2,3,8,16],[32,64,128,256],[512,1024,2048,4096],[8192,2,3,0]]
        
        data = {
            "agent": "human",
            "grid": grid._map,
            "game_over": False,
            "requested_action": "new_game"
        }
        
    elif action == 'run_ai':
        data['agent'] = 'ai'
        grid = Grid(4,4)
        grid._map = data["grid"]
        game = Game(grid, time_limit = TIME_LIMIT) 
        direction, info = game.make_ai_move()
        data["grid"] = game.grid._map
        print(game.grid._map)
        data["search_info"] = info    
        if game.game_over: 
            data["game_over"] = True
            data["agent"] = "human"

        return render_template("grid.html", data = data)
    
    elif action == 'stop_ai':
        data['agent'] = 'human'
    
    elif action == 'human_move':

        dir_dict ={"u": UP, "d": DOWN, "l": LEFT, "r": RIGHT}      
        direction = dir_dict[data["direction"]]
        
        grid = Grid(4,4)
        grid._map = data["grid"]
        game = Game(grid)
        game.make_human_move(direction)
        if game.game_over: 
            data["game_over"] = True
        data["grid"] = game.grid._map     

    return render_template("index.html", data = data)

if __name__ == "__main__":
    app.run(debug=True)