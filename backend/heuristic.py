"""
This is the heuristic used by the mini-max algorithm, when evaluating
grid-positions. 

Given a grid, the quality of the grid is estimated as a combination of 
the monotonicity-score of the grid and the square sum of the grid.
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
    gradient_heuristic
    
    NO STATISTICS:
    Here is the (ordered)performance in 20 consequtive runs with this heuristic (0.6 sec pr move) (max_tile, num_moves):
    [(512,514) (1024,739) (1024,741)(1024,746) (1024,844) (1024,847) (1024,902) (1024,919) (1024,934) (1024,954)
     (1024,973)(2048,1270)(2048,1308)(2048,1348)(2048,1393)(2048,1411)(2048,1614)(2048,1650)(2048,1762)(2048,1780)]
      19 out of 20 gets to the 1024 tile (or above).
      9 out of 20 get to te 2048 tile
      median number of moves is about 963
      
      WITH EXPECTED VALUE: 
      [(1024,950)(1024,963)(1024,974)(2048,1520)(2048,1797)
      (2048,1816),(2048,1883)(4096,3101),(4096,3572),(8192,4619)]
      """
    if len(grid.get_available_moves()) == 0:
        return -10000  # game over is bad
    gh = gradient_heuristic(grid)
    max_tile, ss = square_sum(grid)
    
    score = gh*ss   # I multiply the gradient score (monotonicity) by the value of 
                                  # max_tile/10 to ensure a somewhat constant ratio between gh and ss
    return score

def heuristic_alternative(grid):
    """
    The combined heuristic used by minimax-algorithm 
    Test of the algorithm: 20 games. 
    0.6 sec pr mode
    NO EXPECTECTED VALUE CONSIDERATION
    (512,466)   (1024,714) (1024,736) (1024,765)  (1024,818)(1024,862) (1024,905) (1024,918)(1024,938)(1024,940),
    (1024, 964)(1024, 1002)(2048, 1322)(2048,1345)(2048,1471)(2048,1638)(2048,1705)(2048,1796)(2048,1814)(4096,2498)]
    19 out of 20 gets to the 1024 tile (or above).
    8 out of 20 get to te 2048 tile
    1 gets to the 4096 tile
    median number of moves is about 940
    
    """
    if len(grid.get_available_moves()) == 0:
        return -10000  # game over is bad
    gh = gradient_heuristic(grid)
    max_tile, ss = square_sum(grid)

    score = gh*max_tile/10 + ss   # I multiply the gradient score (monotonicity) by the value of 
                                  # max_tile/10 to ensure a somewhat constant ratio between gh and ss
    return score
  
  
 
  
