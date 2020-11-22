"""
Monotonicity score of grid to be used in heuristic.

Obsolete. Not used in current heuristic function.
"""

def mono_count(row):
    """
    Helper function
    Calculates monotonicity score for single row (or column made vertical)
    """
    count = 0
    for indx, val in enumerate(row[:-1]):
        for val2 in row[indx+1:]:
            if val < val2:
                count += 1
            elif val > val2:
                count -= 1
    return count

def monotonicity(grid):  
    """
    Calculates monotonicity score of entire grid.
    Give preference grids where the values grow in the same direction in all rows (left or right)
    and in the same direction in all columns (up or down) 
    2 4 6 
    4 6 8 
    6 8 10 
    Should give maximal value as all rows grow from left to right and all columns grow downwards. 
    But the direction of growth does not matter
    """
    row_mono = sum(map(mono_count, grid._map))
    cols = [[grid._map[i][j] for i in range(grid._height)] for j in range(grid._width)]

    col_mono = sum(map(mono_count, cols))

    return abs(row_mono) + abs(col_mono)


    