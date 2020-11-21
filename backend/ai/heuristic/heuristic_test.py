import unittest
from .. Grid import Grid, UP, DOWN, LEFT, RIGHT
from monotonicity import mono_count
from monotonicity import monotonicity
from smoothness import smoothness

from gradient_monotonicity import a, v1, v2, v3, v4, v5, v6, v7, tile_sum, gradient_heuristic

from ex import minimax_alpha_beta_DLS, heuristic
import time

class all_tests(unittest.TestCase):

    def test_mono_count(self):
        self.assertEqual(mono_count([1,2]), 1)
        self.assertEqual(mono_count([1,1]), 0)
        self.assertEqual(mono_count([2,1]), -1)

        self.assertEqual(mono_count([1,2,3]), 3)
        self.assertEqual(mono_count([1,2,2]), 2)
        self.assertEqual(mono_count([2,2,2]), 0)
        self.assertEqual(mono_count([2,3,2]), 0)
        self.assertEqual(mono_count([3,3,2]), -2)
        self.assertEqual(mono_count([3,2,2]), -2)
        self.assertEqual(mono_count([4,3,2]), -3)

        self.assertEqual(mono_count([1,2,3,4]), 6)
        self.assertEqual(mono_count([1,2,3,3]), 5)
        self.assertEqual(mono_count([1,3,3,3]), 3)
        self.assertEqual(mono_count([3,3,3,3]), 0)
        self.assertEqual(mono_count([3,2,1,0]), -6)
        self.assertEqual(mono_count([1,2,1,2]), 2)

    def test_monotonicity(self):
        g = Grid(4,4)
        g._map = [
            [2,4,6,8],
            [4,6,8,10],
            [6,8,10,12],
            [8,10,12,14]
        ]  
        self.assertEqual(monotonicity(g), 8*6)
        g = Grid(3,3)
        g._map = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]  
        self.assertEqual(monotonicity(g), 0)
        g._map = [
            [0,0,0],
            [0,0,0],
            [0,0,2]
        ]  
        self.assertEqual(monotonicity(g), 4)

        g._map = [
            [0,0,0],
            [0,0,1],
            [0,0,2]
        ]  
        self.assertEqual(monotonicity(g), 7)

        g._map = [
            [0,0,0],
            [0,0,1],
            [0,1,2]
        ]  
        self.assertEqual(monotonicity(g), 10)

        g._map = [
            [3,0,0],
            [0,0,1],
            [0,1,2]
        ]  
        self.assertEqual(monotonicity(g), 6)

        g._map = [
            [2,1,0],
            [1,0,0],
            [0,0,0]
        ]  
        self.assertEqual(monotonicity(g), 10)
    
    def test_smoothness(self):
        g = Grid(3,3)

        g._map = [
            [0,0,2],
            [0,0,2],
            [0,0,0]
        ]
        self.assertEqual(smoothness(g),1)

        g._map = [
            [2,2,2],
            [2,2,2],
            [2,2,2]
        ]
        self.assertEqual(smoothness(g),12)

        g._map = [
            [0,0,4],
            [0,0,4],
            [0,0,0]
        ]
        self.assertEqual(smoothness(g),2)
        
        g._map = [
            [0,0,4],
            [0,0,4],
            [16,16,0]
        ]
        self.assertEqual(smoothness(g),6)

        g._map = [
            [4,0,4],
            [0,8,0],
            [8,0,0]
        ]
        self.assertEqual(smoothness(g),0)

        g._map = [
            [1024,0,0],
            [1024,0,0],
            [0, 0, 0]
        ]
        self.assertEqual(smoothness(g),10)

        g._map = [
            [1024,0,0],
            [1024,2,0],
            [0, 2, 2]
        ]
        self.assertEqual(smoothness(g),12)

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
        tile_sum = 2
        expected = (v1*2**a)/tile_sum
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)
        grid._map = [
            [2,2,0,0],
            [4,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
        ]
        tile_sum = 2+2+4
        expected = (v1*2**a + v2*2**a + v2*4**a)/tile_sum
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)


        grid._map = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,10,0],
            [0,0,0,0]
        ]
        tile_sum = 10
        expected = (v3*10**a)/tile_sum
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)

        grid._map = [
            [4,2,0,0],
            [2,0,0,0],
            [0,0,10,0],
            [0,0,0,0]
        ]
        tile_sum = 18
        expected = (v1*4**a + v2*2**a + v2*2**a + v5*10**a)/tile_sum
        actual = gradient_heuristic(grid)
        self.assertEqual(actual, expected)

        grid._map = [
            [4,2,0,0],
            [2,0,0,0],
            [0,0,0,0],
            [0,0,0,10]
        ]
        tile_sum = 18
        expected = (v1*10**a + v6*2**a + v6*2**a + v7*4**a)/tile_sum

        actual = gradient_heuristic(grid)
        self.assertAlmostEqual(actual, expected)


if __name__ == "__main__":
    from merge import merge
    from Grid import Grid, UP, DOWN, LEFT, RIGHT
    unittest.main()