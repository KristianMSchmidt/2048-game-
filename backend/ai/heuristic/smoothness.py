from math import log as log

def smoothness(grid):
    """
    Calculates smoothness score of entire grid.
    If two neighbor tiles have same non-zero value
    they will give positive score. 
    2,2 --> 1 point
    4,4 --> 2 points
    8,8 --> 3 points
    Etc.
    """
    score = 0

    for row in grid._map:
        for col in range(grid._width - 1):
            val1 = row[col]
            val2 = row[col + 1]
            if 0 != val1 == val2: # same non-zero value
                score += log(val1)/log(2)

    for col in range(grid._width):
        for row in range(grid._height - 1):
            val1 = grid._map[row][col]
            val2 = grid._map[row + 1][col]
            if 0 != val1 == val2:
                score += log(val1)/log(2)
    
    return score

if __name__ == "__main__":
    from Grid import Grid
    g = Grid(3,3)
    g._map = [
        [2,2,2],
        [2,2,2],
        [2,2,2]
    ]
    print(smoothness(g))
