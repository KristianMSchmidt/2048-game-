"""
Run a test game with AI-player. 
For development purposes. 
"""
from Grid import Grid
from get_move import get_move

def run_test_game():
    g = Grid(4, 4)   
    print(g)    
    for move_num in range(10000):
        print("")
        print("MOVE NUMBER: ", move_num+1)
        print("Grid before move")
        print(g)
        move = get_move(g, time_limit = 0.6)
        print("MOVE FROM GET_MOVE", move)
        if move:
            g.move(move)
            print("Grid after move")
            print(g)
            print("Inserting new tile")
            g.new_tile() # don't forget this!
            print(g)
        else: 
            print("Game over?")
            break
run_test_game()
