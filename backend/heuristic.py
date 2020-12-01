"""
This is the heuristic used by the mini-max algorithm, when evaluating
grid-positions. 

Given a grid, the quality of the grid is estimated as
the monotonicity-score of the grid TIMES the square sum of the grid.
This ensures both monotonicity and an effort to merge high value tiles whenever possible.

After many other attempts, this simple heuristic have proven empirically to be quite good 
"""
from backend.gradient_heuristic import gradient_heuristic

def square_sum(grid):
    """
    Calcultates the sum of the squared tile-values.
    """
    s = 0
    for row in range(4):
        for col in range(4):
                s += grid.get_tile(row,col)**2
    return s

def heuristic(grid):
    """
    The combined heuristic used by minimax-algorithm
    """
    if len(grid.get_available_moves()) == 0:
        return -float('inf')  # game over is bad
    
    return gradient_heuristic(grid) * square_sum(grid)
  
