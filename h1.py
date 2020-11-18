from math import log as log
from gradient_heuristic import heuristic as gradient_heuristic

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

def heuristic(grid):
    h = gradient_heuristic(grid)*smoothness(grid)
    print(h)
    return h