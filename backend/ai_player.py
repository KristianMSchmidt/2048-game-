from Grid import Grid
from get_move import get_move

class AI_player:
    """
    Class to control AI moves and gameplay.
    """
    def __init__(self):        
        self.grid = Grid(4,4)
        self.game_over = False
        self.time_limit = 0.6  # seconds for each move

    def make_move(self):
        """
        Make a single move & update grid with new tile. 
        """
        move = get_move(self.grid, self.time_limit)  # this merely calculates the move
        if move:  #if move is none, the game is over
            self.grid.move(move) # now the grid is actually moved
            self.grid.new_tile() 
            return move
    
    def autoplay(self, verbose = True):
        """
        Let AI play entire game to the end. 
        """
        direction_names = {1: "UP", 2: "DOWN", 3: "LEFT", 4: "RIGHT"}
        if verbose: 
            print("Now autoplaying this grid: ")
            print(self.grid)
        move_num = 1
        while not self.game_over:
            move = self.make_move()
            if move:
                if verbose: 
                    print('Move #{}. Direction: {}. Grid after move:'.format(move_num, direction_names[move]))
                    print(self.grid)
            else: 
                self.game_over = True
                if verbose: 
                    print("Game over?")
            move_num += 1
             

