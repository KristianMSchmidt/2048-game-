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
    
    Testing results (scores from 5 consequtive runs):
    [(max_tile, number of moves)= (2048, 1845), (4096, 3268), (2048, 1641), (2048, 1818), (4096, 3401)]
    """
    if len(grid.get_available_moves()) == 0:
        return 0  # game over -> score = 0 
    gh = gradient_heuristic(grid)
    ss = square_sum(grid)
    score = gh*ss   
    return score

