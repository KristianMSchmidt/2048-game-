"""
Decide next move for AI player by using minimax-algorithm at still deeper levels of search
until time limit is reached.
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
    if not grid.get_available_moves():
        return None

    start_time = time()
    best_move = random_choice(grid.get_available_moves()) # This is important, as search might return None
    score_of_best_move = None
    alpha = - float('inf')   #Best choice for max so far in search
    beta = float('inf')     #Best choice for min so far in search
    time_spend = time() - start_time
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
            time_spend = time() - start_time
        except:
            break
        
    print("Best move:", best_move, "Score:", score_of_best_move, "Depth:",depth-1, "Time Spend:", time()- start_time)
    return best_move





   

    