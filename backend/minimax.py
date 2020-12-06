"""
Get AI-move by recursive, depth-limited minimax search with alpha-beta pruning
"""
from time import time
from backend.heuristic import heuristic

def minimax_alpha_beta_DLS(grid, depth, alpha, beta, start_time, time_limit, first_move, players_turn, do_pruning = True):
    """
    Recursive Depth-Limited minimax search with alpha-beta-pruning.
    Returns (best_score, best_move) found, given the specified depth.

    alpha is best value that a maximing player (perhaps in a higher layer) is already guaranteed to get
    beta is the best value that a minimizing player (perhaps in a higher layer) is already guaranteed to get 
    """

    if time() - start_time > time_limit:
        # If no more time, raise exeption. 
        # This will immediately stop the search at the current depth level. 
        # print("No more time")
        raise Exception("No more time")

    if do_pruning:
        pass
        #assert alpha < beta

    if depth == 0:
        # recursion stops here
        print("depth 0", heuristic(grid), "alpha=", alpha, "beta=", beta)
        return heuristic(grid), first_move

    if players_turn: 
        # This is the maximizing player
        moves = grid.get_available_moves()

        if moves == []:
            return -10000, first_move
        
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
                score, move =  minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, time_limit, first_move = first_move, players_turn = False, do_pruning = do_pruning)
                
            if score >= max_score:
                max_score = score
                max_move = move

            alpha = max(alpha, max_score)     
            print("player", "depth=", depth, score, "alpha=", alpha, "beta=", beta)
            
            if do_pruning and beta <= alpha:
                #
                print("Beta cuf off!", alpha, beta)
                # The reason for the cut is, that the maximizing player will end up with a value
                # that is bigger than the beta, that the minimizing player in a layer above is already guaranteed 
                #to get. So this whole branch is irrelevant. 
                break # cut of branch 

        return max_score, max_move

    else: 
        # Computer's turn (The Minimizing player)
        # What the computer can do is place 2-tile og 4-tile in a free cell
        def get_min_score(grid, cells, alpha, beta):
            min_score = float('inf')
            for cell in cells: 
                child = grid.clone()
                print(cell, 2)
                child.set_tile(cell[0], cell[1], 2)
                score_2, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha,beta, start_time, time_limit, first_move, players_turn = True, do_pruning = do_pruning)
                
                
                print(cell, 4)
                
                child = grid.clone()
                child.set_tile(cell[0], cell[1], 4)
                score_4, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha,beta, start_time, time_limit, first_move, players_turn = True, do_pruning = do_pruning)
                
                score = 0.1*score_4 + 0.9*score_2  # expected value (10% chance for 2, 90% chance for 4)

                if score <= min_score:
                    min_score = score
                beta = min(beta, min_score)   
                print("computer","depth=", depth, cell, "expecte=", score, "alpha=", alpha, "beta=", beta)

                if do_pruning and beta <= alpha:
                    print("Alpha cuf off!", alpha, beta)
                    return min_score #cut of branch
            return min_score
            
        cells = grid.get_available_cells()  #There will always be at least one available cell after a player move
        min_score = get_min_score(grid, cells, alpha, beta)
        return min_score, first_move


