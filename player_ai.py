"""
AI-player for the 2048 game.
"""
#from gradient_heuristic import heuristic 
from h1 import heuristic

import time
import random
# Time Limit For Each Move
time_limit = 0.5
 
class PlayerAI():

    def minimax_alpha_beta_IDDFS(self, grid):
        """
        Minimax with alpha-beta-pruning. Iterative deepening depth-first-search.
        """
        start_time = time.time()
        best_move = random.choice(grid.get_available_moves())
        best_score = - float('inf')
        alpha = - float('inf')   #Best choice for max so far in search
        beta = float('inf')     #Best choice for min so far in search
        depth = 0
        time_spend = time.time() - start_time
       
        while (time_spend < time_limit):
            try:
                score, move = self.minimax_alpha_beta_DLS(grid, depth, True, None, alpha, beta, start_time)
                if move:
                    best_move = move
                    if move != best_move:
                        print("New best move: ", best_move)      
                depth += 1
                
                time_spend = time.time() - start_time
            except:
                break   
        
        print("Best move, depth, time_spend", best_move, depth, time.time()-start_time)
        return best_move
    
    def minimax_alpha_beta_DLS(self, grid, depth, players_turn, first_move, alpha, beta, start_time):
        """
        Recursive Depth-Limited minimax search with alpha-beta-pruning.
        Returns (best_score, best_move) found, given the specified depth.
        """
        if time.time() - start_time > time_limit:
            print("Time is up")
            raise Exception

        if depth == 0:
            return heuristic(grid), first_move

        if players_turn: #This is the maximizing player
            moves = grid.get_available_moves()

            if moves == []:
                return heuristic(grid), first_move

            max_value = (- float('inf'), None)
            for move in moves:
                child = grid.clone()
                child.move(move)
                if first_move == None:
                    value = self.minimax_alpha_beta_DLS(child, depth - 1, False, move, alpha, beta, start_time)
                else:
                    value = self.minimax_alpha_beta_DLS(child, depth - 1, False, first_move, alpha, beta, start_time)
                try:
                    max_value = max(max_value, value)
                except: 
                    max_value = value

                alpha = max(alpha, max_value[0])
                if beta <= alpha:
                    #print "Beta cuf off!"
                    break #cut of branch

            return max_value

        else: # Minimizing player
            cells = grid.get_available_cells()
            min_value = (float('inf'), None)

            for cell in cells:
                child = grid.clone()
                child.set_tile(cell[0], cell[1], 2)
                value_2 = self.minimax_alpha_beta_DLS(child, 
                                depth - 1, True, first_move, alpha,beta, start_time)

                child = grid.clone()
                child.set_tile(cell[0], cell[1], 4)
                value_4 = self.minimax_alpha_beta_DLS(child, 
                                depth - 1, True, first_move, alpha,beta, start_time)

                try:
                    min_value = min(min_value, value_2, value_4)
                except: 
                    raise Exception("min!")

                try:
                    beta = min(beta, min_value[0])
                except: 
                    raise Exception("min2!")

                if beta <= alpha:
                    #print "Alpha cuf off!"
                    break #cut of branch

            return min_value


    def get_move(self, grid):
        """
        Should return 1, 2, 3 or 4, corresponding to UP, DOWN, LEFT or RIGHT.
        """
        if not grid.get_available_moves():
            print("No available moves?")
            print(grid)
            return None
        else: 
            move = self.minimax_alpha_beta_IDDFS(grid)
            return move


if __name__ == "__main__":
    from Grid import Grid
    g = Grid(4, 4)
    
    ai = PlayerAI()    
    for move_num in range(10000):
        print("")
        print("MOVE NUMBER: ", move_num)
        print("GRID BEFORE NOVE:")
        print(g)
        move = ai.get_move(g)
        print("MOVE FROM GET_MOVE", move)
        if move:
            g.move(move)
        else: 
            print("Game over?")
            break
