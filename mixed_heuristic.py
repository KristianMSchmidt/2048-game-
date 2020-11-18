from math import log as log

def heuristic(grid):
    """
    Returns heuristic value of node.
    """
    smooth = smoothness(grid)
    mono = monotonicity(grid)

    zeros = log(len(grid.get_available_cells()))

    max_tile = grid.get_max_tile()
    
    #weights
    w1 = 0.1
    w2 = 1
    w3 = 2.7
    w4 = 1

    #score
    score = w1*smooth + w2*mono + w3*zeros + w4*max_tile 
    return score

def num_moves(grid):

    num_moves = len(grid.get_available_moves())
    if num_moves:
        return num_moves
    else:
        return -float('inf')


def monotonicity(grid):

    def mono_count(row):
        count = 0
        for indx, val in enumerate(row[:-1]):
            for val2 in row[indx+1:]:
                if val < val2:
                    count += 1
                elif val > val2:
                    count -= 1
        return count


    row_mono = sum(map(mono_count, grid._map))
    cols = [[grid._map[i][j] for i in range(4)] for j in range(4)]
    col_mono = sum(map(mono_count, cols))

    return abs(row_mono) + abs(col_mono)

def smoothness(grid):

    score = 0

    for row in range(4):
        row = grid._map[row]
        for col in range(3):
            val1 = row[col]
            val2 = row[col+1]
            if 0 != val1 == val2:
                score += log(val1)/log(2)

    for col in range(4):
        for row in range(3):
            val1 = grid._map[row][col]
            val2 = grid._map[row+1][col]
            if 0 != val1 == val2:
                score += log(val1)/log(2)
    return score

if __name__ == "__main__":
    from Grid import Grid
    g = Grid(4, 4)
    g._map = [
        [40,80,2,2],
        [2,2,2,2],
        [2,2,2,2],
        [2,2,2,2]
    ]
    print(smoothness(g))