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

    def test_get_max_tile(self):
        g = Grid(4,4)

        g._map = [
            [2,2,4,2],
            [2,2,2,2],
            [2,2,2,2],
            [2,2,2,2]
        ]
        self.assertEqual(g.get_max_tile(),4)

        g._map = [   
            [2,2,4,2],
            [2,2,2048,2],
            [2,8,2,2],
            [2,2,2,2]
        ]
        self.assertEqual(g.get_max_tile(),2048)
    
    def test_get_available_cells(self):
        grid = Grid(4,4)
        grid._map = [
            [0,0,0,2],
            [0,1,0,0],
            [0,0,0,0],
            [0,0,0,1]
        ]
        self.assertEqual(len(grid.get_available_cells()),13)
    
    def test_gradient_heuristic(self):
        grid = Grid(4,4)
        grid._map = [
            [2,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        expected = (v1*2)
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)
        grid._map = [
            [2,2,0,0],
            [4,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        expected = (v1*2 + v2*2 + v2*4)
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)


        grid._map = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,10,0],
            [0,0,0,0]
        ]
        expected = (v3*10)
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)

        grid._map = [
            [4,2,0,0],
            [2,0,0,0],
            [0,0,10,0],
            [0,0,0,0]
        ]
        tile_sum = 18
        expected = (v1*4 + v2*2 + v2*2 + v5*10)
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)

        grid._map = [
            [4,2,0,0],
            [2,0,0,0],
            [0,0,0,0],
            [0,0,0,10]
        ]
        expected = v1*10 + v6*2 + v6*2 + v7*4

        actual = gradient_heuristic(grid)
        self.assertAlmostEqual(actual, expected)

class test_grid(unittest.TestCase):

    def test_merge(self):
        """ 
        Testing the merge function 

        From wiki: Tiles slide as far as possible in the chosen direction
        until they are stopped by either another tile or the edge of the 
        grid. If two tiles of the same number collide while moving, they 
        will merge into a tile with the total value of the two tiles that 
        collided. The resulting tile cannot merge with another tile again 
        in the same move. Higher-scoring tiles emit a soft glow.

        If a move causes three consecutive tiles of the same value to slide 
        together, only the two tiles farthest along the direction of motion 
        will combine. If all four spaces in a row or column are filled with
        tiles of the same value, a move parallel to that row/column will 
        combine the first two and last two.
        """
        actual = merge([0,2,4,8])
        expected = [2,4,8,0]
        self.assertEqual(actual, expected)

        actual = merge([0,0,4,8])
        expected = [4,8,0,0]
        self.assertEqual(actual, expected)

        actual = merge([0,0,0,8])
        expected = [8,0,0,0]
        self.assertEqual(actual, expected)

        actual = merge([0,0,0,0])
        expected = [0,0,0,0]
        self.assertEqual(actual, expected)

        actual = merge([2,4,8,16])
        expected = [2,4,8,16]
        self.assertEqual(actual, expected)

        actual = merge([2,2,4,8])
        expected = [4,4,8,0]
        self.assertEqual(actual, expected)

        actual = merge([4,2,2,8])
        expected = [4,4,8,0]
        self.assertEqual(actual, expected)

        actual = merge([4,4,8,0])
        expected = [8,8,0,0]
        self.assertEqual(actual, expected)

        actual = merge([2,2,2,2])
        expected = [4,4,0,0]
        self.assertEqual(actual, expected)

        actual = merge([4,4,16,16])
        expected = [8,32,0,0]
        self.assertEqual(actual, expected)

        actual = merge([2,0,0,2])
        expected = [4,0,0,0]
        self.assertEqual(actual, expected)

        actual = merge([0,4,0,4])
        expected = [8,0,0,0]
        self.assertEqual(actual, expected)

        actual = merge([2,4,0,4])
        expected = [2,8,0,0]
        self.assertEqual(actual, expected)

        actual = merge([0,4,0,4])
        expected = [8,0,0,0]
        self.assertEqual(actual, expected)

        actual = merge([0,4,4,4])
        expected = [8,4,0,0]
        self.assertEqual(actual, expected)

        actual = merge([4,0,4,4])
        expected = [8,4,0,0]
        self.assertEqual(actual, expected)

        actual = merge([8,0,4,4])
        expected = [8,8,0,0]
        self.assertEqual(actual, expected)

        actual = merge([8,8,4,4])
        expected = [16,8,0,0]
        self.assertEqual(actual, expected)

    def test_get_available_moves(self):
        g = Grid(4, 4)
        g._map = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]        
        self.assertEqual(g.get_available_moves(), []) 

        g._map = [
                    [0,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]
                ]
        
        self.assertEqual(g.get_available_moves(), [UP, LEFT]) 

        g._map = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,0,11,12],
                    [13,14,15,16]
                ]
        
        self.assertEqual(g.get_available_moves(), [UP, DOWN, LEFT, RIGHT]) 

        g._map = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,8,11,12],
                    [0,14,15,16]
                ]
        
        self.assertEqual(g.get_available_moves(), [DOWN, LEFT]) 

        g._map = [
                    [1,2,3,4],
                    [5,6,7,0],
                    [9,8,11,12],
                    [13,14,15,16]
                ]
        
        self.assertEqual(g.get_available_moves(), [UP, DOWN, RIGHT]) 

        g._map = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,8,11,12],
                    [13,14,15,0]
                ]
        
        self.assertEqual(g.get_available_moves(), [DOWN, RIGHT]) 

        g._map = [
                    [1,2,3,4],
                    [5,6,7,8],
                    [9,8,11,12],
                    [13,0,15,0]
                ]
        
        self.assertEqual(g.get_available_moves(), [DOWN, LEFT, RIGHT]) 

    def test_move(self):
        g = Grid(3, 3)
        g._map = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]  

        self.assertEqual(g.move(UP), False)
        self.assertEqual(g.move(DOWN), False)
        self.assertEqual(g.move(LEFT), False)
        self.assertEqual(g.move(RIGHT), False)

        g._map = [
            [0,4,8],
            [4,5,6],
            [7,8,9]
        ]  
        self.assertEqual(g.move(DOWN), False)
        self.assertEqual(g.move(RIGHT), False)
        self.assertEqual(g.move(UP), True)
        self.assertEqual(g.get_tile(0,0), 4)
        self.assertEqual(g.move(LEFT), True)
        self.assertEqual(g.get_tile(0,0), 8)
        self.assertEqual(g.move(LEFT), True)
        self.assertEqual(g.get_tile(0,0), 16)

        g._map = [
            [11,4,8],
            [4,5,6],
            [7,8,0]
        ]  
        self.assertEqual(g.move(UP), False)
        self.assertEqual(g.move(LEFT), False)
        self.assertEqual(g.move(RIGHT), True)
        self.assertEqual(g.get_tile(2,2), 8)

        g = Grid(4,4)
        g._map = [
            [8, 4, 2, 2],
            [2, 8, 4, 2],
            [8, 64, 16, 2],
            [256, 4, 128, 8]
        ] 
        self.assertEqual(g.get_available_moves(), [UP, DOWN, LEFT, RIGHT])

        g._map = [
            [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ]  
        self.assertEqual(g.move(UP), False)
        self.assertEqual(g.move(DOWN), False)
        self.assertEqual(g.move(LEFT), False)
        self.assertEqual(g.move(RIGHT), False)

        g._map = [
            [1,2,8,32],
            [1,6,7,8],
            [4,10,11,12],
            [16,14,15,16]
        ]  
        self.assertEqual(g.move(LEFT), False)
        self.assertEqual(g.move(RIGHT), False)

        self.assertEqual(g.move(UP), True)
        self.assertEqual(g.get_tile(0,0), 2)
        self.assertEqual(g.get_tile(1,0), 4)
        self.assertEqual(g.get_tile(2,0), 16)
        self.assertEqual(g.get_tile(0,1), 2)
        self.assertEqual(g.get_tile(0,2), 8)
        self.assertEqual(g.get_tile(0,3), 32)

        self.assertEqual(g.move(LEFT), True)
        self.assertEqual(g.get_tile(0,0), 4)
        self.assertEqual(g.get_tile(0,1), 8)
        self.assertEqual(g.get_tile(0,2), 32)
        self.assertEqual(g.get_tile(1,0), 4)
        self.assertEqual(g.get_tile(2,0), 16)
        
        self.assertEqual(g.move(UP), True)
        self.assertEqual(g.get_tile(0,0), 8)
        self.assertEqual(g.get_tile(1,0), 16)
        self.assertEqual(g.get_tile(0,1), 8)
        self.assertEqual(g.get_tile(0,2), 32)
        
        self.assertEqual(g.move(LEFT), True)
        self.assertEqual(g.get_tile(0,0), 16)
        self.assertEqual(g.get_tile(0,1), 32)
        self.assertEqual(g.get_tile(1,0), 16)

        self.assertEqual(g.move(UP), True)
        self.assertEqual(g.get_tile(0,0), 32)
        self.assertEqual(g.get_tile(0,1), 32)

        self.assertEqual(g.move(LEFT), True)
        self.assertEqual(g.get_tile(0,0), 64)

        g._map = [
            [8,2,8,32],
            [0,6,7,8],
            [0,10,11,12],
            [8,14,15,16]
        ]  
        self.assertEqual(g.move(UP), True)
        self.assertEqual(g.get_tile(0,0),16)
        
        g._map = [
            [8,2,8,32],
            [31,6,7,8],
            [0,10,11,12],
            [8,7,0,7]
        ]  
        self.assertEqual(g.move(RIGHT), True)
        self.assertEqual(g.get_tile(3,3),14)
        self.assertEqual(g.get_tile(3,2),8)

        g = Grid(3,3)
        g._map = [
            [2,2,2],
            [2,2,4],
            [6,2,2]
           ]
        g.move(RIGHT)
        self.assertEqual(g.get_tile(0,1),2)
        self.assertEqual(g.get_tile(0,2),4)
        self.assertEqual(g.get_tile(1,1),4)
        self.assertEqual(g.get_tile(1,2),4)
        self.assertEqual(g.get_tile(2,1),6)
        self.assertEqual(g.get_tile(2,2),4)

        g = Grid(3,3)
        g._map = [
            [2,2,2],
            [2,2,4],
            [6,2,2]
           ]
        g.move(DOWN)
        self.assertEqual(g.get_tile(2,0),6)
        self.assertEqual(g.get_tile(2,1),4)
        self.assertEqual(g.get_tile(2,2),2)
        self.assertEqual(g.get_tile(1,0),4)
        self.assertEqual(g.get_tile(1,1),2)
        self.assertEqual(g.get_tile(1,2),4)


        g = Grid(3,3)
        g._map = [
            [2,2,2],
            [2,2,4],
            [6,2,4]
           ]
        g.move(UP)
        self.assertEqual(g.get_tile(0,0),4)
        self.assertEqual(g.get_tile(0,1),4)
        self.assertEqual(g.get_tile(0,2),2)
        self.assertEqual(g.get_tile(1,0),6)
        self.assertEqual(g.get_tile(1,1),2)
        self.assertEqual(g.get_tile(1,2),8)

        g = Grid(3,3)
        g._map = [
            [2,2,2],
            [2,2,4],
            [6,2,2]
           ]
        g.move(LEFT)
        self.assertEqual(g.get_tile(0,0),4)
        self.assertEqual(g.get_tile(1,0),4)
        self.assertEqual(g.get_tile(2,0),6)
        self.assertEqual(g.get_tile(0,1),2)
        self.assertEqual(g.get_tile(1,1),4)
        self.assertEqual(g.get_tile(2,1),4)

    def test_clone(self):
        g = Grid(3,3)
        g._map = [
            [2,2,2],
            [2,2,4],
            [6,2,2]
        ]
        clone = g.clone()
        self.assertEqual(clone._map, g._map)
        clone.move(UP)
        self.assertNotEqual(clone._map, g._map)

class test_minimax(unittest.TestCase):
        
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
                    beta = float('inf'), start_time = time(), time_limit = 5, first_move = None, players_turn = True)
        expected = (heuristic(grid), None)
        self.assertEqual(actual, expected)

        # DEPTH 1: PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = None, players_turn = True)
        
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
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = None, players_turn = True)
        expected = (heuristic(grid), None)
        self.assertEqual(actual, expected)

        # DEPTH 1: PLAYERS TURN
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = None, players_turn = True)
        
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
        val = min(0.9*child_00_2_val + 0.1* child_00_4_val, 0.9*child_12_2_val +  0.1* child_12_4_val)
        expected = val, UP
        actual = minimax_alpha_beta_DLS(grid, depth = 1, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = UP, players_turn = False)
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
                    beta = float('inf'), start_time = time(), time_limit = 5,first_move = UP, players_turn = True)
        self.assertEqual(actual, expected)      


        # First_move = UP, computer sets value 4 in empty cell 
        child_up_4 = child_up.clone()
        child_up_4.set_tile(3, 0, 4)
        self.assertEqual(child_up_4.get_available_cells(), []) # assert game over in this branch
        UP4_val = heuristic(child_up_4)

        # Computer chooses lowest score in UP branch
        UP_val = 0.9*UP2_val + 0.1*UP4_val 
        actual = minimax_alpha_beta_DLS(child_up, depth = 2, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = UP, players_turn = False)
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
                    beta = float('inf'), start_time = time(), time_limit = 5,first_move = LEFT, players_turn = True)
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
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = LEFT, players_turn = True)
        self.assertEqual(actual, expected)      

        #computer chooses min value in left-branch
        LEFT_val = 0.9*LEFT2_val + 0.1* LEFT4_val
        expected = LEFT_val, LEFT
        actual = minimax_alpha_beta_DLS(child_left, depth = 2, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = LEFT, players_turn = False)
        self.assertEqual(actual, expected)      

        #Finally, player chooses max and move
        val = max(UP_val, LEFT_val)
        expected = val, LEFT
        actual = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                    beta = float('inf'), start_time = time(),time_limit = 5, first_move = None, players_turn = True)
        self.assertEqual(actual, expected)     


        # Now we test, that alpha-beta-pruning does not affect resulting score and move 
        
        grid = Grid(4,4)
        grid._map = [
            [2, 4, 4, 2],
            [8, 2, 4, 16],
            [2, 2, 0, 0],
            [2, 2, 8, 4]
        ]    
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 5,
                first_move = UP, players_turn = False, do_pruning =True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 2, alpha = -float('inf'), 
               beta = float('inf'), start_time = time(), time_limit = 5,
                first_move = UP, players_turn = False, do_pruning = False)
        
        self.assertEqual(with_pruning, no_pruning)
        
        
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
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = True, do_pruning = False)
        
        self.assertEqual(with_pruning, no_pruning)

        grid = Grid(4,4)
        grid._map = [
            [16,2,4,2],
            [2,2,2,4],
            [8,32,16,8],
            [2,64,2,8]
        ]       

        with_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = None, players_turn = True, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = None, players_turn = True, do_pruning = False)
        self.assertEqual(with_pruning, no_pruning)


        grid._map = [
            [0,2,30,2],
            [4,12,18,4],
            [8,14,20,26],
            [10,2,22,28]
        ]   

        with_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 5,
                first_move = None, players_turn = True, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 3, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 5,
                first_move = None, players_turn = True, do_pruning = False)

        self.assertEqual(with_pruning, no_pruning)
        
        grid = Grid(4,4)
        grid._map=[
            [0, 0, 0, 4],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 2, 0]]
        

        with_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = None, players_turn = True, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 10,
                first_move = None, players_turn = True, do_pruning = False)
        self.assertEqual(with_pruning, no_pruning)
        
        grid = Grid(4,4)
        grid._map=[
            [2, 0, 0, 4],
                    [0, 0, 2, 0],
                    [0, 0, 0, 0],
                    [0, 0, 2, 0]]
        
        
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 4, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 15,
                first_move = None, players_turn = False, do_pruning = False)
        self.assertEqual(with_pruning, no_pruning)
        
        grid = Grid(4,4)
        grid._map=[
            [2, 2, 0, 4],
            [0, 4, 2, 0],
            [4, 0, 0, 0],
            [0, 8, 2, 0]]
        
        
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 1500,
                first_move = None, players_turn = False, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 1500,
                first_move = None, players_turn = False, do_pruning = False)
        
        self.assertEqual(with_pruning, no_pruning)
        
        grid = Grid(4,4)
        grid._map = [
            [0,2,4,2],
            [2,0,0,0],
            [8,0,16,8],
            [2,0,16,8]
        ]       
        
        with_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
            beta = float('inf'), start_time = time(), time_limit = 200, first_move = None, 
            players_turn = True, do_pruning = True)
        
        no_pruning = minimax_alpha_beta_DLS(grid, depth = 5, alpha = -float('inf'), 
                beta = float('inf'), start_time = time(), time_limit = 200,
                first_move = None, players_turn = True, do_pruning = False)





    def test_get_move(self):
        g = Grid(4,4)

        #Game over should return none
        g._map = [
            [16,2,30,2],
            [4,12,18,4],
            [8,14,2,26],
            [10,2,22,28]
        ] 
        self.assertEqual(get_move(g), None)

if __name__ == "__main__":
    unittest.main()
   
