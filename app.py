# Setup instuctions for Flask in Visual Studio Code
# 1) Make folder/directory for flask project
# 2) Go to this folder and open terminal 
# 3) Write command "python -m venv env" (this makes the virtual environment)
# 4) Ctrl + Shift + P --> Python select intrepreter --> select the one with "env"   
# 5) In therminal: "pip install flask"
# 6) In terminal: "python app.py"

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
        #grid._map = [[2,4,8,16],[32,64,128,256],[512,1024,2048,4096],[8192,0,0,0]]
        
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
        game.make_ai_move()
        data["grid"] = game.grid._map    
        if game.game_over: 
            data["game_over"] = True
            data["agent"] = "human"
                
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