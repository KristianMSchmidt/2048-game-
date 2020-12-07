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
            [2,2,16,0]
        ]
        
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)
        
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        
        
        self.assertEqual(with_pruning, no_pruning)
    
        
        """
        grid2 = grid.clone()
        
        grid2._map = [
            [2,2,2,2],
            [2,2,4,2],
            [8,16,2,8],
            [2,2,16,0]
        ]
        
        with_pruning = minimax_alpha_beta_DLS(grid2, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid2, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)

        grid2up=grid2.clone()
        grid2up.move(UP)
        
        with_pruning = minimax_alpha_beta_DLS(grid2up, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid2up, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid2down=grid2.clone()
        grid2down.move(DOWN)
        
        with_pruning = minimax_alpha_beta_DLS(grid2down, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid2down, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid2left=grid2.clone()
        grid2left.move(LEFT)
        
        with_pruning = minimax_alpha_beta_DLS(grid2left, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid2left, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid2right=grid2.clone()
        grid2right.move(RIGHT)
        
        with_pruning = minimax_alpha_beta_DLS(grid2right, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid2right, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid4 = grid.clone()
        
        grid4._map = [
            [2,2,2,2],
            [2,2,4,2],
            [8,16,4,8],
            [2,2,16,0]
        ]
        
        with_pruning = minimax_alpha_beta_DLS(grid4, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid4, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)

        grid4up=grid4.clone()
        grid4up.move(UP)
        
        with_pruning = minimax_alpha_beta_DLS(grid4up, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid4up, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid4down=grid4.clone()
        grid4down.move(DOWN)
        
        with_pruning = minimax_alpha_beta_DLS(grid4down, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid4down, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid4left=grid4.clone()
        grid4left.move(LEFT)
        
        with_pruning = minimax_alpha_beta_DLS(grid4left, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid4left, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        #print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        
        grid4right=grid4.clone()
        grid4right.move(RIGHT)
        
        with_pruning = minimax_alpha_beta_DLS(grid4right, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)

        no_pruning = minimax_alpha_beta_DLS(grid4right, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        print(no_pruning)
        self.assertEqual(with_pruning, no_pruning)
        """
        
        
        
       
    
        

if __name__ == "__main__":
    unittest.main()
   