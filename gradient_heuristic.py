"""
This heuristic assigns high values to grid-positions, where tiles with heigh values
are concentrated in one of the four corners.  

The weights have not yet been fine tuned (perhaps this could be done by Reinforcement learning?)
"""

# Weights
v1 = 4
v2 = 2
v25 = 1
v3 = 0
v4 = -0.25
v5 = -0.5
v6 = -1
v7 = -1.5

# Gradient tables
UL = {(0,0):v1,    (0,1):v2,   (0,2):v3,    (0,3):v4,
      (1,0):v2,    (1,1):v25,   (1,2):v4,    (1,3):v5,
      (2,0):v3,    (2,1):v4,   (2,2):v5,    (2,3):v6,
      (3,0):v4,    (3,1):v5,   (3,2):v6,    (3,3):v7}


UR = {(0,0):v4,    (0,1):v3,   (0,2):v2,    (0,3):v1,
      (1,0):v5,    (1,1):v4,   (1,2):v25,    (1,3):v2,
      (2,0):v6,    (2,1):v5,   (2,2):v4,    (2,3):v3,
      (3,0):v7,    (3,1):v6,   (3,2):v5,    (3,3):v4}


LL = {(0,0):v4,    (0,1):v5,   (0,2):v6,    (0,3):v7,
      (1,0):v3,    (1,1):v4,   (1,2):v5,    (1,3):v6,
      (2,0):v2,    (2,1):v25,   (2,2):v4,    (2,3):v5, 
      (3,0):v1,    (3,1):v2,   (3,2):v3,    (3,3):v4}


LR = {(0,0):v7,    (0,1):v6,   (0,2):v5,    (0,3):v4,
      (1,0):v6,    (1,1):v5,   (1,2):v4,    (1,3):v3,
      (2,0):v5,    (2,1):v4,   (2,2):v25,    (2,3):v2,
      (3,0):v4,    (3,1):v3,   (3,2):v2,    (3,3):v1}

      
def heuristic(grid):
    if not grid.get_available_moves():
      return - float('inf')

    ur = 0
    ul = 0
    lr = 0
    ll = 0

    for row in range(4):
          for col in range(4):
                cell = (row, col)
                val = grid.get_tile(row, col)
                ur += UR[cell] * val**2
                ul += UL[cell] * val**2
                lr += LR[cell] * val**2
                ll += LL[cell] * val**2
    
    best_score = max(ur, ul, lr, ll)

    
    return best_score

if __name__ == "__main__":
    from Grid import Grid
    g = Grid(4, 4)
    print(g)
    print(heuristic(g))
    print(UL)