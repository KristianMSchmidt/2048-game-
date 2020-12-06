"""
Unit testing of back-end (all functions, classes and methods)
"""
import unittest
from time import time

from backend.Grid import Grid, UP, DOWN, LEFT, RIGHT, merge
from backend.gradient_heuristic import v1, v2, v3, v4, v5, v6, v7, gradient_heuristic
from backend.heuristic import heuristic
from backend.minimax import minimax_alpha_beta_DLS
from backend.get_move import get_move
    
class test_heuristics(unittest.TestCase):
    
    

    def test_minimax__aplha_beta_DLS(self):
        
     # Now we test, that alpha-beta-pruning does not affect resulting score and move 
        grid = Grid(4,4)
        grid._map = [
            [2, 4, 4, 2],
            [8, 2, 4, 16],
            [2, 2, 0, 0],
            [2, 2, 8, 4]
        ]    
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = UP, players_turn = False, do_pruning =True)
        print("Pruning", with_pruning)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = -float('inf'), 
               beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = UP, players_turn = False, do_pruning = False)
        #print("No pruning", no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
              # Now we test, that alpha-beta-pruning does not affect resulting score and move 
        grid = Grid(4,4)
        grid._map = [
            [0,2,4,2],
            [2,0,0,0],
            [8,0,16,8],
            [2,0,16,8]
        ]       
        
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = True)
        
       # no_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
        #""        beta = float('inf'), start_time = time(), time_limit = 15,
         #       first_move = None, players_turn = True, do_pruning = False)
        
        #self.assertEqual(with_pruning, no_pruning)

    
    
        

if __name__ == "__main__":
    unittest.main()
   