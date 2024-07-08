import numpy as np




def count_neighbours(grid, y, x):
    height, width = grid.shape

    start_row, end_row = max(x-1, 0), min(x+2, width)
    start_col, end_col = max(y-1, 0), min(y+2, height)
    
    subgrid = grid[start_col:end_col, start_row:end_row]
    
    if grid[y, x] == 1:
        return np.count_nonzero(subgrid == 1) - 1
    else:
        return np.count_nonzero(subgrid == 1)
    


def live_or_die(grid, y, x):
    alive = grid[y, x]
    neighbour_count = count_neighbours(grid, y, x)
    if alive:
        return 1 if 2 <= neighbour_count <= 3 else 0
    else:
        return 1 if neighbour_count == 3 else 0
    




def update_grid(grid):
    # check each index of grid
    height, width = grid.shape
    new_grid = np.zeros((height, width))    
    
    for y in range(height):
        for x in range(width):
            new_grid[y, x] = live_or_die(grid, y, x)
            
    return new_grid







# Test cases
if __name__ == '__main__':
    rounds = 6
    grid = np.array([[0,1,1,0,0],
                     [0,1,0,0,0],
                     [0,1,0,0,0],
                     [0,0,0,0,0]])

    for round_index in range(rounds+1):
        print('Round', round_index)
        print(grid) 

        grid = update_grid(grid)    
    
       
            


    