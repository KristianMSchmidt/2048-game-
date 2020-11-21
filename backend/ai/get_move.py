"""
"""

from minimax import minimax_alpha_beta_IDDFS
 
def get_move(self, grid):
    """
    Should return 1, 2, 3 or 4 (UP, DOWN, LEFT or RIGHT).
    Or None, if no available moves (game over)
    """
    if not grid.get_available_moves():
        return None

    else: 
        move = self.minimax_alpha_beta_IDDFS(grid)
        return move

if __name__ == "__main__":
    from Grid import Grid
    g = Grid(4, 4)
    ai = PlayerAI()
    print(g)    
    print(monotonicity(g))
    for move_num in range(10000):
        print("")
        print("MOVE NUMBER: ", move_num+1)
        move = ai.get_move(g)
        print("MOVE FROM GET_MOVE", move)
        if move:
            g.move(move)
            g.new_tile()
            print(g)
        else: 
            print("game over?")
            break
