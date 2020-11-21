"""
Minimax
"""
import time
import random

# Time Limit For Each Move
time_limit = 10
 
    
def minimax_alpha_beta_DLS(grid, depth, alpha, beta, start_time, first_move, players_turn, do_pruning = True):
    """
    Recursive Depth-Limited minimax search with alpha-beta-pruning.
    Returns (best_score, best_move) found, given the specified depth.

    alpha is least value that a maximing player (perhaps in a higher layer) is already guaranteed to get
    beta is the best value that a minimizing player (perhaps in a higher layer) is already guaranteed to get 
    """
    if time.time() - start_time > time_limit:
        # If no more time, raise exeption. 
        # This will immediately stop the search at the current depth level. 
        raise Exception
    if do_pruning:
        assert alpha < beta

    if depth == 0:
        # recursion stops here
        return heuristic(grid), first_move

    if players_turn: 
        # This is the maximizing player
        moves = grid.get_available_moves()

        if moves == []:
            return heuristic(grid), first_move
        
        max_score = - float('inf')
        max_move = None
        for move in moves:
            # Clone the grid and make move
            child = grid.clone()
            child.move(move)

            if first_move == None:
                # Computers turn (the minimizing player). Returns the worst case scenario after current move
                score, move =  minimax_alpha_beta_DLS(child,depth-1,alpha, beta, start_time, first_move = move, players_turn = False, do_pruning = do_pruning)
            else: 
                # Computers turn - returns the worst case scenario after current move
                score, move =  minimax_alpha_beta_DLS(child, depth - 1, alpha, beta, start_time, first_move = first_move, players_turn = False, do_pruning = do_pruning)
                
            if score >= max_score:
                max_score = score
                max_move = move

            alpha = max(alpha, max_score)     
            
            if do_pruning and beta <= alpha:
                #print("Beta cuf off!", alpha, beta)
                # The reason for the cut is, that the maximizing player will end up with a value
                # that is bigger than the beta, that the minimizing player in alayer above is guaranteed 
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
                for tile_value in [2, 4]: # computer sets 2 and 4 in free cell
                    child.set_tile(cell[0], cell[1], tile_value)
                    score, _ = minimax_alpha_beta_DLS(child, depth - 1, alpha,beta, start_time, first_move, players_turn = True, do_pruning = do_pruning)
                    if score <= min_score:
                        min_score = score
                    beta = min(beta, score)    
                    if do_pruning and beta <= alpha:
                        #print("Alpha cuf off!", alpha, beta)
                        return min_score #cut of branch
            return min_score
            
        cells = grid.get_available_cells()  #There will always be at least one available cell after a player move
        min_score = get_min_score(grid, cells, alpha, beta)
        return min_score, first_move


if __name__ == "__main__":
    from Grid import Grid
    grid = Grid(4,4)
    grid._map = [
            [0,2,30,2],
            [2,16,18,4],
            [8,14,20,26],
            [10,2,22,28]
        ]   
    
    start_time = time.time()     
    actual = minimax_alpha_beta_DLS(grid, depth = 12, alpha = -float('inf'), 
            beta = float('inf'), start_time = time.time(), first_move = 2,
             players_turn = False, do_pruning = False)
    print(time.time()-start_time)
    
    start_time = time.time()     
    actual = minimax_alpha_beta_DLS(grid, depth = 12, alpha = -float('inf'), 
            beta = float('inf'), start_time = time.time(), first_move = 2,
             players_turn = False, do_pruning = True)
    print(time.time()-start_time)
    