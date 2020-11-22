import random
from copy import deepcopy

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
OFFSETS = {UP: (1, 0), DOWN: (-1, 0), LEFT: (0, 1), RIGHT: (0, -1)}

class Grid:
    """
    Class to control the basic game logic - moves, new tiles, etc.
    """
    def __init__(self, grid_height, grid_width):
        """
        Initialize grid.
        """
        self._height = grid_height
        self._width = grid_width
        self.reset()
        up_tiles = [(0, colon) for colon in range(grid_width)]
        down_tiles = [(grid_height - 1, colon) for colon in range(grid_width)]
        left_tiles =  [(row, 0) for row in range(grid_height)]
        right_tiles = [(row, grid_width - 1) for row in range(grid_height)]
        self._initial_tiles = {UP: up_tiles, DOWN: down_tiles, LEFT: left_tiles, RIGHT: right_tiles}
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        s = str(self._height) + "x" + str(self._width) + " grid: \n"
        for row in self._map:
            s += str(row) + "\n"
        return(s)

    def reset(self):
        """
        Reset the game so the grid is empty except for two initial tiles.
        """
        zero_map = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self._map = zero_map
        self.new_tile()
        self.new_tile()

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
    
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._map[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._map[row][col]
    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        if random.random() < 0.9:
            tile_value = 2
        else:
            tile_value = 4

        while True:
            tile_row = random.randrange(self._height)
            tile_col = random.randrange(self._width)

            if self.get_tile(tile_row, tile_col) == 0:
                self.set_tile(tile_row,tile_col,tile_value)
                return ()

    def get_max_tile(self):
        """
        Fetches the maximal tile value 
        """
        max_tile = 0

        for row in range(self._height):
            for col in range(self._width):
                max_tile = max(max_tile, self._map[row][col])

        return max_tile
    
    def get_available_cells(self):
        """
        Fetches list of tuples of the empty cells
        """
        cells = []
        for row in range(self._height):
            for col in range(self._width):
                if self._map[row][col] == 0:
                    cells.append((row, col))
        return cells

    def clone(self):
        """
        Make a Deep Copy of This Object
        """
        gridCopy = Grid(self._height, self._width)
        gridCopy._map = deepcopy(self._map)
        gridCopy._height = self._height
        gridCopy._width = self._width        
        return gridCopy

    def move(self, direction):
        """
        Move all tiles in the given direction. 
        Return true if change has happened. Else false.
        """
        if direction in [UP, DOWN]:
            len_of_lists_to_be_merged = self._height
        
        else:
            len_of_lists_to_be_merged = self._width

        changed = False

        for tile in self._initial_tiles[direction]:
            to_be_merged = []
            for step in range(len_of_lists_to_be_merged):
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                to_be_merged.append(self.get_tile(row, col))

            merged = merge(to_be_merged)
           
            for step in range(len_of_lists_to_be_merged):
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                if self.get_tile(row, col) != merged[step]:
                    changed = True
                self.set_tile(row, col, merged[step])

        return changed

    # Return All Available Moves
    def get_available_moves(self):
        available_moves = []

        for dir in [UP, DOWN, LEFT, RIGHT]:
            gridCopy = self.clone() 
            if gridCopy.move(dir):
                available_moves.append(dir)

        return available_moves

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    non_zeros = []
    zeros = []
    tiles = []
    actual_is_tiled = False

    for number in line:
        if number != 0:
            non_zeros.append(number)
        else:
            zeros.append(0)

    for index in range(len(non_zeros)):
        actual = non_zeros[index]

        if actual_is_tiled:
            zeros.append(0)
            actual_is_tiled = False
        
        elif index < len(non_zeros) - 1:
            next_num=non_zeros[index + 1]
            if actual != next_num:
                tiles.append(actual)
            else:
                tiles.append(actual + next_num)
                actual_is_tiled = True
        else:
            tiles.append(actual)

    return tiles + zeros


