"""
Decide next move for AI player by using minimax-algorithm at still deeper levels of search
until time limit is reached. The chosen move will be the one reached a the deepest level of
search.
"""
from backend.minimax import minimax_alpha_beta_DLS 
from time import time as time
from random import choice as random_choice

def get_move(grid, time_limit = 0.6):
    """
    Minimax with alpha-beta-pruning. 
    Iterative deepening depth-first-search.
    
    Should return 1, 2, 3 or 4 (UP, DOWN, LEFT or RIGHT).
    Or None, if no available moves (game over)
    """
    available_moves = grid.get_available_moves()
    
    if not available_moves:
        return None
    alpha = -float('inf')
    beta = float('inf')
    start_time = time()
    #best_move = random_choice(available_moves) # This is important, as search might return None
    score_of_best_move = None
    depth = 0
       
    while True:
        try:
            depth += 1
            score, move = minimax_alpha_beta_DLS(grid, depth, alpha, beta, start_time, 
                time_limit, first_move=None, players_turn=True, do_pruning = True)
            if move:
                best_move = move
                score_of_best_move = score
                #print(depth, best_move, score_of_best_move)
        except:
            break
    info = "Best move:{} Score:{} Depth:{} Time Spend: {}".format(best_move, score_of_best_move, depth-1, time()- start_time)
    print(info)
    return best_move, info





   

    