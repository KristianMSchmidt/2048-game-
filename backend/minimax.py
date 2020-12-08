"""
Get AI-move by recursive, depth-limited minimax search
"""
from time import time
from backend.heuristic import heuristic

def minimax_alpha_beta_DLS(grid, depth,  alpha, beta, start_time, time_limit, first_move, 
                           players_turn, do_pruning=False, two_branch_score=False):
    """
    Recursive Depth-Limited minimax search with pruning.
    Returns (best_score, best_move) found, given the specified depth.
    
    alpha is a max-score that the maximizing player in the loop above is already guaranteed to get
    beta is a min-score, that the minimizing player in the loop above is already guaranteed to get 
    
    pruning won't change results, but will give a significant (5x-ish) speed-up of the search
    (its optional for testing purposes)
    """

    if time() - start_time > time_limit:
        # If no more time, raise exeption. 
        # This will immediately stop the search at the current depth level. 
        raise Exception("No more time")

    if depth == 0:
        # recursion stops here
        return heuristic(grid), first_move

    if players_turn: 
        # This is the maximizing player 
        moves = grid.get_available_moves()

        if moves == []:
            return 0, first_move  # game over -> score = 0
        
        max_score = - float('inf')  
        max_move = None
        alpha = max_score

        for move in moves:
            # Clone the grid and make move
            child = grid.clone()
            child.move(move)
            # Pass on resulting grid to the minimizing player (the computer)
            if first_move == None:
                score, move =  minimax_alpha_beta_DLS(child,depth-1, alpha, beta, start_time, time_limit, first_move = move, players_turn = False, do_pruning = do_pruning)
            else: 
                score, move =  minimax_alpha_beta_DLS(child, depth-1, alpha, beta, start_time, time_limit, first_move = first_move, players_turn = False, do_pruning=do_pruning)
            if score > max_score: 
                max_score = score
                max_move = move   
                alpha = score
                #--> indentation

            if do_pruning:                
                if not two_branch_score: # We are in a 2-branch (a branch where the minimizing player has
                                        # has placed a tile wile value 2 in a free cell. This happens with
                                        #  90% likelihood)
                    if 0.9*score >= beta:  # In this case, the expected value score 0.9*score_2 + 0.1*score_4
                                           # is guaranteed to be bigger than the beta, that the minimizing player
                                           # above is already guaranteed to get - so further search in this branch
                                           # is irrelevant, as minimizing player will not choose from this branch 
                        #print("pruning 2-branch")
                        break
                    
                if two_branch_score: # We are in the 4-branch with a recorded score of 2-branch
                    exp_score_at_least = 0.9*two_branch_score + 0.1*score # the expected score of the cell in layer above 
                                                                          #will be at least this value
                    if  exp_score_at_least >= beta:  # same explanation as above
                        #print("pruning 4-branch")                        
                        break
                                
        return max_score, max_move

    else: 
        # Computer's turn (The Minimizing player)
        # What the computer can do is place 2-tile og 4-tile in one of the free cell
        cells = grid.get_available_cells()  #There will always be at least one available cell after
                                            #a player move
        min_score = float('inf')
        beta = min_score
        for cell in cells:
            # clone grid and place 2-tile in the free cell
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 2)
            # pass on resulting grid to maximizing player and get result
            score_2, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time,
                            time_limit, first_move, players_turn = True,
                            do_pruning=do_pruning, two_branch_score = False)
            if do_pruning:
                if 0.9*score_2 >= min_score:  #no reason to inspect 4-branch for this cell, as final value of
                                              # the expected score of the cell will not be the minimal one
                   #print("pruning 4-branch in this cell:", cell)
                   continue

            # clone grid and place 4-tile in the free cell                         
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 4)    
            # pass on resulting grid to maximizing player and get result
            score_4, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move, players_turn = True, do_pruning=do_pruning, two_branch_score=score_2)

            score =  0.9*score_2 + 0.1*score_4  # expected value of cell (10% chance for 2, 90% chance for 4)
            min_score = min(min_score, score)
            beta = min_score
            
            if do_pruning:
                if score <= alpha: # In this case the minimum is guaranteed to be smaller that
                                  # than what a maximizing player in a loop above is already guaranteed to get
                                  # so it's irrelevant to continue searching for smaller values in this direction
                                  # since the maximizing player will not choose from this branch
                    #print("alpha pruning")
                    break
            
        return min_score, first_move


