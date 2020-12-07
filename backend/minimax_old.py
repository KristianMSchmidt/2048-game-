"""
Get AI-move by recursive, depth-limited minimax 
"""
from time import time
from backend.heuristic import heuristic
verbose = False
def minimax_alpha_beta_DLS(grid, depth,  alpha, beta, start_time, time_limit, first_move, players_turn, do_pruning=False, two_branch_score=False):
    """
    Recursive Depth-Limited minimax search with alpha-beta-pruning.
    Returns (best_score, best_move) found, given the specified depth.
    
    alpha is the least score, that maximizing player is already guaranteed to get
    beta is a lowest score, that minimizing player is already guaranteed to get 
    """
    if verbose: 
        print("Depth=",depth)

    if time() - start_time > time_limit:
        # If no more time, raise exeption. 
        # This will immediately stop the search at the current depth level. 
        raise Exception("No more time")

    if depth == 0:
        if verbose: 
            print("depth=", depth, "alpha=", alpha, "beta=", beta, "score", "score=", heuristic(grid))
    
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
                score, move =  minimax_alpha_beta_DLS(child, depth-1, alpha, beta, start_time, time_limit, first_move = first_move, players_turn = False, do_pruning=do_pruning)

            if depth == 1:
                print (move, score, "alpha=", alpha, "beta=", beta)

            if score >= max_score:
                max_score = score
                max_move = move
                alpha = max(max_score, alpha)    
            if do_pruning:
                if not two_branch_score:
                    #print("two-branch")
                    if score*0.9 >= beta: 
                        #print("PRUNING 2-branch", score, 0.9*score, beta)
                        #pass
                        break #return max_score, max_move  # Cut branch! the max found by this maximizing player is bigger than 
                        # the lowest score a minimizing player above is already guaranteed to get,
                        # so further search for max is irrelevant
                else:
                 #   print("This is four branch")
                    exp_score_at_least = 0.1*score + 0.9*two_branch_score 
                    if  exp_score_at_least >= beta:
                        print("PRUNING 4-branch!", exp_score_at_least, ">=", beta)                        
                        #pass
                        break #return max_score, max_move
                        
        if depth == 3:
            print ("max_move, max_score", max_move, max_score)       
        return max_score, max_move

    else: 
        # Computer's turn (The Minimizing player)
        # What the computer can do is place 2-tile og 4-tile in a free cell
        cells = grid.get_available_cells()  #There will always be at least one available cell after a player move
        min_score = float('inf')
        for cell in cells:
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 2)
            if depth ==2:
                print(cell, 2, "alpha=", alpha, "beta=", beta)
            score_2, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move, players_turn = True, do_pruning=do_pruning, two_branch_score = False)
            # Her var der tidligere opdatering af beta of pruning. Det skal der vel også være her?
            child = grid.clone()
            child.set_tile(cell[0], cell[1], 4)
            
            if depth ==2:
               print(cell, 4, "alpha=", alpha, "beta=", beta)
    
            score_4, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move, players_turn = True, do_pruning=do_pruning, two_branch_score=score_2)

            #print("score_4", score_4)       

            score = 0.1*score_4 + 0.9*score_2  # expected value (10% chance for 2, 90% chance for 4)
            if depth == 2:
                print(cell, "s2=",score_2, "s4=",score_4, "exp=",score, "alpha=", alpha, "beta=",beta)
            #print("expected score", score)
            if score <= min_score:
                min_score = score
                beta = min(min_score, beta)
            
        return min_score, first_move


