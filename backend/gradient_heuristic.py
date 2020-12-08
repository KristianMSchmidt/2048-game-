"""
This function assigns high values to grid-positions, where tile-values grow toward one
of the four corners - i.e. it encourage "monotonicity" of the grid. 

Grids like this one will get a high score, and will thus be favored by the AI-player

32 16 8 4
16 8  4 2
8  4 2 0
2  2 0 0.

The weights could probably be fined tuned to get even better results, but the values below have
proven to work quite well
"""

# Weights 
v1 = 11.4 #1.5**6
v2 = 7.6 #1.5**5
v3 = 3.4 # 1.5**3
v4 = 2.2  #1.5**2
v5 = 1.5   #1.5
v6 = 1   #1
v7 = 0

# Gradient tables
UL = {(0,0):v1,    (0,1):v2,   (0,2):v3,    (0,3):v4,
      (1,0):v2,    (1,1):v3,   (1,2):v4,    (1,3):v5,
      (2,0):v3,    (2,1):v4,   (2,2):v5,    (2,3):v6,
      (3,0):v4,    (3,1):v5,   (3,2):v6,    (3,3):v7}

UR = {(0,0):v4,    (0,1):v3,   (0,2):v2,    (0,3):v1,
      (1,0):v5,    (1,1):v4,   (1,2):v3,    (1,3):v2,
      (2,0):v6,    (2,1):v5,   (2,2):v4,    (2,3):v3,
      (3,0):v7,    (3,1):v6,   (3,2):v5,    (3,3):v4}

LL = {(0,0):v4,    (0,1):v5,   (0,2):v6,    (0,3):v7,
      (1,0):v3,    (1,1):v4,   (1,2):v5,    (1,3):v6,
      (2,0):v2,    (2,1):v3,   (2,2):v4,    (2,3):v5, 
      (3,0):v1,    (3,1):v2,   (3,2):v3,    (3,3):v4}

LR = {(0,0):v7,    (0,1):v6,   (0,2):v5,    (0,3):v4,
      (1,0):v6,    (1,1):v5,   (1,2):v4,    (1,3):v3,
      (2,0):v5,    (2,1):v4,   (2,2):v3,    (2,3):v2,
      (3,0):v4,    (3,1):v3,   (3,2):v2,    (3,3):v1}
      
def gradient_heuristic(grid):
   
    ur = 0
    ul = 0
    lr = 0
    ll = 0

    for row in range(4):
          for col in range(4):
                cell = (row, col)
                val = grid.get_tile(row, col)
                ur += UR[cell] * val
                ul += UL[cell] * val
                lr += LR[cell] * val
                ll += LL[cell] * val
    
    best_score = max(ur, ul, lr, ll)
    
    return best_score

