from time import time
from random import choice as random_choice

from minimax import minimax_alpha_beta_DLS

def minimax_alpha_beta_IDDFS(self, grid):
    """
    Minimax with alpha-beta-pruning. Iterative deepening depth-first-search.
    """
    start_time = time()
    best_move = random_choice(grid.get_available_moves())
    depth = -1
    score_of_best_move = None
    alpha = - float('inf')   #Best choice for max so far in search
    beta = float('inf')     #Best choice for min so far in search
    time_spend = time() - start_time
            
    while (time_spend < time_limit):
        try:
            depth += 1
            score, move = self.minimax_alpha_beta_DLS(grid, depth, True, None, alpha, beta, start_time)
            if move:
                best_move = move
                score_of_best_move = score
            time_spend = time() - start_time
        except:
            break   
    
    print("Best move, score, depth, time_spend", best_move, score_of_best_move, depth, time.time()-start_time)
    return best_move