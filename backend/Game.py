from backend.Grid import Grid
from backend.get_move import get_move

class Game:
    """
    Class to control gameplay and AI moves.
    """
    def __init__(self, grid = None, time_limit = 0.6):
        if grid:
            self.grid = grid
        else:          
            self.grid = Grid(4,4)
        self.game_over = False
        self.time_limit = time_limit  # seconds for each move

    def make_human_move(self, direction):
        """
        Move grid in the given direction (if possible) & update grid with new tile (if move is made)
        """
        if direction in self.grid.get_available_moves():
            self.grid.move(direction) 
            self.grid.new_tile() # After each move, add a new tile
            if len(self.grid.get_available_moves()) == 0:
                self.game_over = True

    def make_ai_move(self):
        """
        Calculate ai move, make move & update grid with new tile. 
        """
        direction, info = get_move(self.grid, self.time_limit)  # this merely calculates the move
    
        if direction:  # if direction is none, the game is over
            self.grid.move(direction) 
            self.grid.new_tile() # After each move, add a new tile
        else: 
            self.game_over = True
        return direction, info

            
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
            direction, info = self.make_ai_move()
            if direction: 
                if verbose: 
                    print('Move #{}. Direction: {}. Grid after move:'.format(move_num, direction_names[direction]))
                    print(self.grid)
                move_num += 1
        print("Game over")
        return self.grid.get_max_tile(), move_num

             

