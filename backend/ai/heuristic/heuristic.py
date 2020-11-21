from gradient_monotonicity import 
def heuristic(grid):
    max_tile = grid.get_max_tile()
    if max_tile == 2048:
        return float('inf')
    elif len(grid.get_available_moves()) == 0:
        return -float('inf')
    else: 
        return monotonicity(grid)

# four available moves is better than 2
# free cells?
# måske summen af værdierne i anden i en separat heuristik? så skal a=1