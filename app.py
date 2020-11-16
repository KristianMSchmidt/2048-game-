# Setup instuctions for Flask in Visual Studio Code
# 1) Make folder/directory for flask project
# 2) Go to this folder and open terminal 
# 3) Write command "python -m venv env" (this makes the virtual environment)
# 4) Ctrl + Shift + P --> Python select intrepreter --> select the one with "env"   
# 5) In therminal: "pip install flask"
# 6) In terminal: "python app.py"

from flask import Flask, render_template, request
#import timeit, json
#from random import choice as random_choice
#from backend.Puzzle import Puzzle
#from backend.utils import convert_solution_string
#from backend.puzzle_collection import eight_puzzles, fifteen_puzzles

app = Flask('__name__')

@app.route("/", methods=['GET', 'POST'])
def index():
    return "2048"


if __name__ == "__main__":
    app.run(debug=True)