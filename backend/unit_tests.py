import unittest
from Grid import Grid, UP, DOWN, LEFT, RIGHT
from merge import merge
from monotonicity import mono_count
from monotonicity import monotonicity
from smoothness import smoothness

from mixed_heuristic import heuristic as mixed_heuristic
from gradient_heuristic import a, v1, v2, v3, v4, v5, v6, v7, tile_sum, gradient_heuristic

from ex import minimax_alpha_beta_DLS, heuristic
import time

class all_tests(unittest.TestCase):
        
    def test_minimax__aplha_beta_DLS(self):
        grid = Grid(4,4)
        grid._map = [
            [2,2,30,32],
            [4,12,18,24],
            [8,14,20,26],
            [10,16,22,28]
        ]        

        # DEPTH 0 : PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 0, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = None, players_turn = True)
        expected = (heuristic(grid), None)
        self.assertEqual(actual, expected)

        # DEPTH 1: PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = None, players_turn = True)
        
        child3 = grid.clone()
        child3.move(3)
        h3 = heuristic(child3)

        child4 = grid.clone()
        child4.move(4)
        h4 = heuristic(child4)
        if h4 > h3:
            expected = h4, 4
        else: 
            expected = h3, 3
        self.assertEqual(actual, expected)   

        grid._map = [
            [0,2,30,32],
            [4,12,18,24],
            [8,14,20,26],
            [10,16,22,28]
        ]        

        # DEPTH 0: PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 0, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = None, players_turn = True)
        expected = (heuristic(grid), None)
        self.assertEqual(actual, expected)

        # DEPTH 1: PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = None, players_turn = True)
        
        child_left = grid.clone()
        child_left.move(LEFT)
        h_left = heuristic(child_left)

        child_up = grid.clone()
        child_up.move(UP)
        h_up = heuristic(child_up)
 
        if h_left > h_up:
            expected = h_left, LEFT
        else: 
            expected = h_up, UP

        self.assertEqual(actual, expected)           
        

        # DEPTH 1: COMPUTERS TURN

        # Computer has more than one available tile
        grid._map = [
            [0,2,30,2],
            [4,12,0,4],
            [8,14,20,26],
            [10,2,22,28]
        ]        

        # cell = (0,0) value 2
        child_00_2 = grid.clone()
        child_00_2.set_tile(0, 0, 2)
        child_00_2_val = heuristic(child_00_2)

        # cell = (0,0) value 4
        child_00_4 = grid.clone()
        child_00_4.set_tile(0, 0, 4)
        child_00_4_val = heuristic(child_00_4)


        #cell = (1,2) value 2
        child_12_2 = grid.clone()
        child_12_2.set_tile(1, 2, 2)
        child_12_2_val = heuristic(child_12_2)
 
        #cell = (1,2) value 4
        child_12_4 = grid.clone()
        child_12_4.set_tile(1, 2, 4)
        child_12_4_val = heuristic(child_12_4)

        # computer chooses minimal value
        val = min(child_00_2_val, child_00_4_val, child_12_2_val, child_12_4_val)
        expected = val, UP
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = UP, players_turn = False)
        self.assertEqual(actual, expected)      
 

        # DEPTH 3: PLAYERS TURN
        grid._map = [
            [0,2,30,2],
            [4,12,18,4],
            [8,14,20,26],
            [10,2,22,28]
        ]        

        # first_move = UP
        child_up = grid.clone()
        child_up.move(UP)
       
        #first_move = UP, computer sets value 2 in empty cell
        child_up_2 = child_up.clone()
        child_up_2.set_tile(3, 0, 2)
       
        #first_move = UP, computer sets value 2 in empty cell, then player moves left
        child_up_2_left = child_up_2.clone()
        child_up_2_left.move(LEFT)
        UP2LEFT_val = heuristic(child_up_2_left)

        #first_move = UP, computer sets value 2 in empty cell, then player moves right
        child_up_2_right = child_up_2.clone()
        child_up_2_right.move(RIGHT)
        UP2RIGHT_val = heuristic(child_up_2_right)
        
        # Player chooses highest value in UP2 branch
        UP2_val = max(UP2LEFT_val, UP2RIGHT_val)
        expected = UP2_val, UP
        actual = minimax_alpha_beta_DLS(child_up_2, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = UP, players_turn = True)
        self.assertEqual(actual, expected)      


        # First_move = UP, computer sets value 4 in empty cell 
        child_up_4 = child_up.clone()
        child_up_4.set_tile(3, 0, 4)
        self.assertEqual(child_up_4.get_available_cells(), []) # assert game over in this branch
        UP4_val = heuristic(child_up_4)

        # Computer chooses lowest score in UP branch
        UP_val = min(UP2_val, UP4_val) 
        actual = minimax_alpha_beta_DLS(child_up, depth = 2, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = UP, players_turn = False)
        expected = (UP_val, UP)
        self.assertEqual(actual,expected )

        # first_move = LEFT
        child_left = grid.clone()
        child_left.move(LEFT)
       
        #first_move = LEFT, computer sets value 2 in empty cell 
        child_left_2 = child_left.clone()
        child_left_2.set_tile(0, 3, 2)

        #first_move = LEFT, computer sets value 2 in empty cell, player moves left 
        child_left_2_left = child_left_2.clone()
        child_left_2_left.move(LEFT)
        LEFT2LEFT_val = heuristic(child_left_2_left)

        #first_move = LEFT, computer sets value 2 in empty cell, player moves right 
        child_left_2_right = child_left_2.clone()
        child_left_2_right.move(RIGHT)
        LEFT2RIGHT_val = heuristic(child_left_2_right)

        #player chooses max in left-2-branch
        LEFT2_val = max(LEFT2LEFT_val, LEFT2RIGHT_val)
        expected = LEFT2_val, LEFT
        actual = minimax_alpha_beta_DLS(child_left_2, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = LEFT, players_turn = True)
        self.assertEqual(actual, expected)      

        #first_move = LEFT, computer sets value 4 in empty cell 
        child_left_4 = child_left.clone()
        child_left_4.set_tile(0, 3, 4)

        #first_move = LEFT, computer sets value 4 in empty cell, player moves down 
        child_left_4_down = child_left_4.clone()
        child_left_4.move(DOWN)
        LEFT4DOWN_val = heuristic(child_left_4_down)

        #first_move = LEFT, computer sets value 4 in empty cell, player moves up 
        child_left_4_up = child_left_4.clone()
        child_left_4.move(UP)
        LEFT4UP_val = heuristic(child_left_4_up)

        #player chooses max in left-4-branch
        LEFT4_val = max(LEFT4DOWN_val, LEFT4UP_val)
        expected = LEFT4_val, LEFT
        actual = minimax_alpha_beta_DLS(child_left_4, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = LEFT, players_turn = True)
        self.assertEqual(actual, expected)      

        #computer chooses min value in left-branch
        LEFT_val = min(LEFT2_val, LEFT4_val)
        expected = LEFT_val, LEFT
        actual = minimax_alpha_beta_DLS(child_left, depth = 2, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = LEFT, players_turn = False)
        self.assertEqual(actual, expected)      

        #Finally, player chooses max and move
        val = max(UP_val, LEFT_val)
        expected = val, LEFT
        actual = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time.time(), first_move = None, players_turn = True)
        self.assertEqual(actual, expected)     


        # Now we test, that alpha-beta-pruning does not affect resulting score and move 
        grid = Grid(4,4)
        grid._map = [
            [0,2,4,2],
            [2,0,0,0],
            [8,0,16,8],
            [2,0,16,8]
        ]       
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = False)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = True)
        self.assertEqual(with_pruning, no_pruning)

        grid = Grid(4,4)
        grid._map = [
            [16,2,4,2],
            [2,2,2,4],
            [8,32,16,8],
            [2,64,2,8]
        ]       

        with_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = False)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = True)
        self.assertEqual(with_pruning, no_pruning)


        grid._map = [
            [0,2,30,2],
            [4,12,18,4],
            [8,14,20,26],
            [10,2,22,28]
        ]   

        with_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = False)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time.time(), 
                first_move = None, players_turn = True, do_pruning = True)
        self.assertEqual(with_pruning, no_pruning)

unittest.main()
   
