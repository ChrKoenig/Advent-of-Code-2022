import re
import os
import time

def get_neighbors(i, j, cells_visited):
    elev = grid[i][j]
    if elev == "S":
        elev = "a"

    neighbors = []

    if i > 0 and (i-1, j) not in cells_visited and ord(grid[i-1][j]) <= ord(elev) + 1:
        neighbors.append((i-1, j))
    if j < len(grid[0])-1 and (i, j+1) not in cells_visited and ord(grid[i][j+1]) <= ord(elev) + 1:
        neighbors.append((i, j+1))
    if i < len(grid)-1 and (i+1, j) not in cells_visited and ord(grid[i+1][j]) <= ord(elev) + 1:
        neighbors.append((i+1, j))
    if j > 0 and (i, j-1) not in cells_visited and ord(grid[i][j-1]) <= ord(elev) + 1:
        neighbors.append((i, j-1))
    
    return neighbors

def print_grid(frontier, cells_visited):
    grid_print = ""
    for i, s in enumerate(grid):
        for j, c in enumerate(s):
            if (i,j) in cells_visited:
                grid_print += "."
            elif (i,j) in frontier:
                grid_print += "X"
            else:
                grid_print += c
    print('\n'.join(re.findall('.{1,143}', grid_print)))
    print("\n ################ \n")

if __name__ == "__main__":
    # Initialize grid
    clear = lambda: os.system('cls')
    grid = open('data/data_12_12.txt', 'r').read().split('\n')

    # Part 1
    # for i, _ in enumerate(grid):
    #     for j, _ in enumerate(grid[1]):
    #         if grid[i][j] == "S":
    #             start = (i,j)
    #         elif grid[i][j] == "E":
    #             end = (i,j)

    # frontier = [start]
    
    # Part 2
    frontier = []
    for i, _ in enumerate(grid):
        for j, _ in enumerate(grid[1]):
            if grid[i][j] == "a":
                frontier.append((i,j))
            elif grid[i][j] == "E":
                end = (i,j)

    cells_visited = []
    path_length = 0
    shortest_path = 0

    while shortest_path == 0 and len(frontier) > 0:
        # clear()
        # print_grid(frontier, cells_visited)
        cells_visited = cells_visited + frontier
        new_frontier = []
        path_length += 1
        for cell in frontier:
            neighbors = get_neighbors(cell[0], cell[1], cells_visited)
            for neighbor in neighbors:
                if neighbor == end:
                    if grid[cell[0]][cell[1]] in ["y", "x"]:
                        shortest_path = path_length
                    continue
                if neighbor not in new_frontier:
                    new_frontier.append(neighbor) 
                if neighbor not in cells_visited:
                    cells_visited.append(neighbor)
    
        frontier = new_frontier

    print(shortest_path)
   