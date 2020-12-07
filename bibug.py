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
    
        grid = Grid(4,4)
      
        grid._map = [
            [2,2,2,2],
            [2,2,4,2],
            [8,16,0,8],
            [2,2,16,4]
        ]
        grid.move(LEFT)
        print(grid)
        #[4, 4, 0, 0]
        #[4, 4, 2, 0]
        #[8, 16, 8, 0]
        #[4, 16, 4, 0]
        print("NO PRUNING")
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = 279206, 
                beta = 573004, start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        
        print("WITH PRUNING")
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = 279206, 
                beta = 573004, start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)
       
        print(with_pruning)
        print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
if __name__ == "__main__":
    unittest.main()
   