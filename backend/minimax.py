"""
Get AI-move by recursive, depth-limited minimax 
"""
from time import time
from backend.heuristic import heuristic

def minimax_alpha_beta_DLS(grid, depth,  alpha, beta, start_time, time_limit=0.6, first_move=None, players_turn=True, do_pruning=False):
    """
    Recursive Depth-Limited minimax search with alpha-beta-pruning.
    Returns (best_score, best_move) found, given the specified depth.
    
    alpha is the least score, that maximizing player is already guaranteed to get
    beta is a lowest score, that minimizing player is already guaranteed to get 
    """

    if time() - start_time > time_limit:
        # If no more time, raise exeption. 
        # This will immediately stop the search at the current depth level. 
        # print("No more time")
        raise Exception("No more time")

    if depth == 0:
        # recursion stops here
        return heuristic(grid), first_move

    if players_turn: 
        # This is the maximizing player
        moves = grid.get_available_moves()

        if moves == []:
            return 0, first_move  # 0 is the heuristic score of a "game over" grid
        
        max_score = - float('inf')
        max_move = None
        for move in moves:
            # Clone the grid and make move
            child = grid.clone()
            child.move(move)

            if first_move == None:
                # Computers turn (the minimizing player). Returns the worst case scenario after current move
                score, move =  minimax_alpha_beta_DLS(child,depth-1, alpha, beta, start_time, time_limit, first_move = move, players_turn = False, do_pruning = do_pruning)
            else: 
                # Computers turn - returns the worst case scenario after current move
                score, move =  minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move = first_move, players_turn = False, do_pruning=do_pruning)
                
            if score >= max_score:
                max_score = score
                max_move = move

        return max_score, max_move

    else: 
        # Computer's turn (The Minimizing player)
        # What the computer can do is place 2-tile og 4-tile in a free cell
        cells = grid.get_available_cells()  #There will always be at least one available cell after a player move
        min_score = float('inf')
        for cell in cells: 
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 2)
            score_2, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move, players_turn = True, do_pruning=do_pruning)
                    
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 4)
            score_4, _ = minimax_alpha_beta_DLS(child, depth - 1, start_time, time_limit, first_move, players_turn = True, do_pruning=do_pruning)
            
            score = 0.1*score_4 + 0.9*score_2  # expected value (10% chance for 2, 90% chance for 4)

            if score <= min_score:
                min_score = score
            
        return min_score, first_move


