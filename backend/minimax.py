"""
Get AI-move by recursive, depth-limited mini-max search
"""
from time import time
from backend.heuristic import heuristic

def minimax_alpha_beta_DLS(grid, depth, alpha, beta, start_time, time_limit, first_move, 
                           players_turn, do_pruning=False, two_branch_score=False):
    """
    Recursive Depth-Limited minimax search with pruning.

    When players_turn = True, it will return (best_score, best_move) found in a search with the given depth.
    
    alpha is a max-score that the maximizing agent (the player) in the loop above is already guaranteed to get
    beta is a min-score, that the minimizing player (the computer) in the loop above is already guaranteed to get 
    
    Pruning won't change results, but will give a significant (5x-ish) speed-up of the search
    (its optional for testing purposes)
    """

    if time() - start_time > time_limit:
        # If no more time, raise exception. 
        # This will immediately stop the search at the current depth level. 
        raise Exception("No more time")

    if depth == 0:
        # Recursion stops here
        return heuristic(grid), first_move

    if players_turn: 
        # It is the maximizing player's turn

        # We start out be getting af list of available moves.
        moves = grid.get_available_moves()

        if moves == []:
            # If there are no available moves, the game is over (max_score = 0)
            max_score = 0
            return max_score, first_move  

        max_score = - float('inf') # The maximal score we can get from one of the available moves.  
        alpha = max_score
        max_move = None  # The move that maximizes the score (will only be used in the first/original loop.)

        for move in moves:
            # Clone the grid and make move
            child = grid.clone()
            child.move(move)

            # Pass on resulting grid to the minimizing player (the computer)
            if first_move == None:
                score, branch_first_move =  minimax_alpha_beta_DLS(
                    child, depth-1, alpha, beta, start_time, time_limit, first_move=move, players_turn=False, do_pruning=do_pruning)
            else: 
                score, branch_first_move =  minimax_alpha_beta_DLS(
                    child, depth-1, alpha, beta, start_time, time_limit, first_move=first_move, players_turn=False, do_pruning=do_pruning)

            # Update max_score, alpha and max_move
            if score > max_score: 
                max_score = score
                alpha = max_score
                max_move = branch_first_move

            # Do pruning of search tree if possible
            if do_pruning:                
                if not two_branch_score: # We are in a 2-branch (a branch where the minimizing player has
                                         # placed a tile wile value 2 in a free cell. This happens with
                                         # 90% likelihood)
                    if 0.9*score >= beta:  # In this case, the expected value score 0.9*score_2 + 0.1*score_4
                                           # is guaranteed to be bigger than the score beta, that the minimizing player
                                           # above is already guaranteed to get - so further search in this branch
                                           # is irrelevant, as minimizing player will not choose from this branch 
                        break # Pruning!
                    
                if two_branch_score: # We are in the 4-branch with a recorded score of the 2-branch
                    exp_score_at_least = 0.9*two_branch_score + 0.1*score #
                    if  exp_score_at_least >= beta:  
                        # No reason to keep searching in this branch (same explanation as above)                          
                        break  # Pruning!
                                
        return max_score, max_move

    else: 
        # It is the minimizing agents's turn (the computer's turn)
        # What the computer can do is place 2-tile og 4-tile in one of the free cell
        
        # We start out by getting a list of free cells
        # (There will always be at least one available cell after a player move)
        cells = grid.get_available_cells()  

        min_score = float('inf') # The minimal score the minizing agent can get by choosing one of the available cells. 
        beta = min_score

        for cell in cells:
            
            # clone grid and place a 2-tile in the free cell
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 2)
            
            # pass on the resulting grid to the maximizing player and get result
            score_2, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time,
                            time_limit, first_move, players_turn = True,
                            do_pruning=do_pruning, two_branch_score = False)

            # Do pruning of search tree if possible: 
            if do_pruning:
                if 0.9*score_2 >= min_score:  # no reason to inspect 4-branch for this cell, as final value of
                                              # the expected score of the cell will not be the minimal one
                   continue

            # clone grid and place 4-tile in the free cell                         
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 4)    

            # pass on resulting grid to maximizing player and get result
            score_4, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, 
                            time_limit, first_move, players_turn = True, 
                            do_pruning=do_pruning, two_branch_score=score_2)

            # calculate expexted value of cell (90% chance for 2-tile, 10% chance for 4-tile)
            score =  0.9*score_2 + 0.1*score_4  
            min_score = min(min_score, score)

            # Do pruning of search tree if possible:
            if do_pruning:
                if score <= alpha: # In this case the minimum is guaranteed to be smaller
                                  # than what a maximizing player in a loop above is already guaranteed to get
                                  # so it's irrelevant to continue searching for smaller values in this direction
                                  # since the maximizing player will not choose from this branch
                    break
            
        return min_score, first_move


