"""
This is the heuristic used by the mini-max algorithm, when evaluating
grid-positions. 

Given a grid, the quality of the grid is estimated as a combination of 
the monotonicity-score of the grid TIMES the square sum of the grid.
This ensures both monotonicity and an effort to merge high value tiles whenever possible.

After many other attempts, this simple heuristic have proven empirically to be quite good 
"""
from backend.gradient_heuristic import gradient_heuristic

def square_sum(grid):
    """
    Calcultates the sum of the squared tile-values.
    """
    squaresum = 0
    max_tile = 2
    for row in range(4):
        for col in range(4):
            tile_val = grid.get_tile(row, col) 
            squaresum += tile_val**2
            if tile_val > max_tile:
                max_tile = tile_val
            
    return max_tile, squaresum

def heuristic(grid):
    """
    The combined heuristic used by minimax-algorithm
    """
    if len(grid.get_available_moves()) == 0:
        return -float('inf')  # game over is bad
    gh = gradient_heuristic(grid)
    max_tile, ss = square_sum(grid)

    score = gh*max_tile/10 + ss   # I multiply the gradient score (monotonicity) by the value of 
                                  # max_tile/10 to ensure a somewhat constant ratio between gh and ss
    return score
  