"""
This is the heuristic used by the mini-max algorithm, when evaluating
grid-positions. 

Given a grid, the quality of the grid is estimated as the product of the gradient-heuristic of the grid
and the square sum of the grid. Taking the product ensures that the score of a grid is proportional to
both the gradient-heuristic score score and the square-sum of the grid.
"""
from backend.gradient_heuristic import gradient_heuristic

def square_sum(grid):
    """
    Calcultates the sum of the squared tile-values. Using this score in the final heuristic will
    encourage AI-player to merge high-value tiles into tiles with even higher numbers.
    """
    squaresum = 0
    for row in range(4):
        for col in range(4):
            tile_val = grid.get_tile(row, col) 
            squaresum += tile_val**2            
    return squaresum

def heuristic(grid):
    """
    The combined heuristic used by the AI-player (i.e. in the minimax-algorithm). 
       
    Testing. 20 consequetive runs gave these results: 
    [max_tile, num_moves]= 
    [(4096, 3290), (4096, 3675), (2048, 1658), (2048, 1516), (2048, 1779)]
    [(4096, 3864), (4096, 3172), (2048, 1180), (4096, 2700), (2048, 1666)]
    [(2048, 1775), (2048, 1449), (1024, 909), (2048, 1665), (2048, 1854)]
    [(1024, 1024), (4096, 3196), (4096, 2819), (4096, 2874), (4096, 2777)]
    """
    if len(grid.get_available_moves()) == 0:
        return 0  # game over -> score = 0 
    gh = gradient_heuristic(grid)
    ss = square_sum(grid)
    score = gh*ss   
    return score



