import unittest
from Grid import Grid
from Grid import UP, DOWN, LEFT, RIGHT
from player_ai import PlayerAI
from mixed_heuristic import heuristic as mixed_heuristic
from gradient_heuristic import heuristic as gradient_heuristic
from merge import merge

class test_grid(unittest.TestCase):

    def test_merge(self):
        """ Testing the merge function 
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
            combine the first two and last two."""

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

    def test_move3x3(self):
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
        self.assertEqual(g.move(DOWN), False)
        self.assertEqual(g.get_tile(2,2), 8)

        g._map = [
            [8, 4, 2, 2],
            [2, 8, 4, 2],
            [8, 64, 16, 2],
            [256, 4, 128, 8]
        ] 
        self.assertEqual(g.get_available_moves(), [UP, DOWN, LEFT, RIGHT])

    def test_move3x3(self):
        g = Grid(4, 4)
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


if __name__ == '__main__':
    unittest.main()

   
