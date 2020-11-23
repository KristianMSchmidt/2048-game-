  class test_monotonicity(unittest.TestCase):

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
        
    

